from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=250, unique=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    slug = models.SlugField(max_length=240, unique=True, editable=False, null=False)
    # slug = AutoSlugField(populate_from='title')
    book_cover = CloudinaryField('image', default='placeholder')
    

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    review_text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    star_rating = models.IntegerField()
    purchase_link = models.CharField(max_length=300, blank=True)
    

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title


    
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('review_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
   
   

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentauthor"
    )
   
    comment_text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ["published_on"]

    def __str__(self):
        return f"Comment text is: {self.comment_text}"


class WishlistItem(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                             related_name="wishlist")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="wishlistowner"
    )
   
    book_marked_as_read = models.BooleanField(default=False)
    published_on = models.DateTimeField(auto_now_add=True)

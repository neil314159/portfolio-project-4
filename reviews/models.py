from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    # slug = models.SlugField(max_length=250, unique=True)
    slug = AutoSlugField(populate_from='title')
    book_cover = CloudinaryField('image', default='placeholder')
    

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    review_text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    star_rating = models.IntegerField()
    purchase_link = models.CharField(max_length=300)
    

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title


    def slugify_function(self, content):
        return content.replace('_', '-').lower()
    

    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.slug)])
   

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

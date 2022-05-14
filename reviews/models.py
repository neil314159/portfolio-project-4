from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from django.utils.text import slugify

STAR_RATING = (
    (1, "⭐"),
    (2, "⭐⭐"),
    (3, "⭐⭐⭐"),
    (4, "⭐⭐⭐⭐"),
    (5, "⭐⭐⭐⭐⭐"),
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=250, unique=False, verbose_name="Book Title")
    book_author = models.CharField(max_length=200, verbose_name="Book Author")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    slug = models.SlugField(max_length=240, unique=True, editable=False, null=False)
    # slug = AutoSlugField(populate_from='title')
    # book_cover = CloudinaryField('image', default='placeholder')
    book_cover = CloudinaryField('image', blank=True, transformation={'width': '625', 'height': '1000', 'crop': 'fill', 'gravity': "auto"}, default=("https://res.cloudinary.com/dpsodnurd/image/upload/v1652284886/m6mvsjkb3eqpn2wczqsu.jpg"))

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1, verbose_name="Book Category")
    review_text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    # star_rating = models.IntegerField()
    star_rating = models.IntegerField(choices=STAR_RATING, default=5)
    purchase_link = models.URLField(max_length=400, blank=True, verbose_name="Purchase Link URL")
    

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

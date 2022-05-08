from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=200)
    

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
    

    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    review_text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    star_rating = models.IntegerField()
    purchase_link = models.URLField(max_length=250)
    


    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title


    def slugify_function(self, content):
        return content.replace('_', '-').lower()
   

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author"
    )
   
    comment_text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ["published_on"]

    def __str__(self):
        return f"Comment text is: {self.comment_text}"


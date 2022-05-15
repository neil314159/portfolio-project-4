from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


""" Emoji strings used for star ratings"""
STAR_RATING = (
    (1, "⭐"),
    (2, "⭐⭐"),
    (3, "⭐⭐⭐"),
    (4, "⭐⭐⭐⭐"),
    (5, "⭐⭐⭐⭐⭐"),
)


class Category(models.Model):
    """Stores categories for book reviews"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    """Main model holding book reviews"""
    title = models.CharField(max_length=250, unique=False,
                             verbose_name="Book Title")
    book_author = models.CharField(max_length=200, verbose_name="Book Author")
    """ Link to user """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
   
    """ Cloudinary field to store book cover"""
    book_cover = CloudinaryField('image', blank=True,
                                 transformation={
                                                 'width': '625',
                                                 'height': '1000',
                                                 'crop': 'fill',
                                                 'gravity': "auto"
                                                 },
                                 default=("https://res.cloudinary.com/dpsodnurd/image/upload/v1652618629/zhtctppqjky78q8h760n.jpg"))
    """ Link to book category"""
    category = models.ForeignKey(
                                 Category, on_delete=models.PROTECT,
                                 default=1, verbose_name="Book Category")
    """ Main text of review """
    review_text = models.TextField()
    """ Date of publication"""
    published_on = models.DateTimeField(auto_now_add=True)
    """ Star rating out of 5"""
    star_rating = models.IntegerField(choices=STAR_RATING, default=5)
    """ Link to purchase book externally"""
    purchase_link = models.URLField(
                                    max_length=400, blank=True,
                                    verbose_name="Purchase Link URL"
                                    )

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns address of article"""
        return reverse('review_detail', args=[str(self.id)])


class Comment(models.Model):
    """ Blog comments model"""
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentauthor"
    )
    """ Main text of comment"""
    comment_text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["published_on"]

    def __str__(self):
        return f"Comment text is: {self.comment_text}"
    
    # def get_absolute_url(self):
    #     """ Returns address of article"""
    #     return reverse('review_detail', args=[str(self.review.id)])


class WishlistItem(models.Model):
    """ Item for wishlist stores user and book review together"""
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name="wishlist")
    author = models.ForeignKey(
                               User, on_delete=models.CASCADE,
                               related_name="wishlistowner"
                              )

    book_marked_as_read = models.BooleanField(default=False)
    published_on = models.DateTimeField(auto_now_add=True)

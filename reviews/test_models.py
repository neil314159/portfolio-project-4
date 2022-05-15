from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Review, Category, Comment, WishlistItem


class SetUpTestCases(TestCase):
    """ Configure test case setup for all other test cases """

    def setUp(self):
        """ Initial configuration """
        self.username = 'neil'
        self.password = 'secretpass'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password)
        """ Log in client """
        self.client.login(username='neil', password='secretpass')
        """ Create instances of models used"""
        self.category = Category.objects.create(name='Science')

        self.review = Review.objects.create(
            title="Origin of Species",
            book_author="Charles Darwin",
            category=self.category,
            author=self.user,
            review_text="excellent!",
            published_on='Jan. 21, 2022, 9:00 a.m.',
            star_rating=3,
        )
        self.comment = Comment.objects.create(
            author=self.user,
            published_on='Jan. 21, 2022, 9:00 a.m.',
            review=self.review,
            comment_text="Here's a comment"
        )
        self.wishlist = WishlistItem.objects.create(
            author=self.user,
            published_on='Jan. 21, 2022, 9:00 a.m.',
            review=self.review,
            book_marked_as_read=False
        )


class SelfNameTestCase(SetUpTestCases):
    def test_category_name(self):
        self.assertEqual(str("Science"), self.category.__str__())

    def test_comment_string(self):
        self.assertEqual(str("Here's a comment"), self.comment.__str__())

    def test_review_name(self):
        self.assertEqual(str("Origin of Species"), self.review.__str__())

    def test_absolute_url(self):
        self.assertEqual(self.review.get_absolute_url(), reverse(
            'review_detail', kwargs={'pk': self.review.id}))

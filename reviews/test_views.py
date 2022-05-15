from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Review, Category, Comment, WishlistItem
from .views import wishlist_toggle_read


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


class BookRatingView(SetUpTestCases):
    """ Test response HTML codes for each view"""

    def test_review_listing_page_status_code(self):

        url = reverse('reviews')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_Review_listing_uses_correct_template(self):
        """ Test if using correct template """
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_book_list_view_for_logged_in_user(self):
        """ check correct editing view shown to logged in user"""
        response = self.client.get(reverse(
            'review_edit', kwargs={'pk': self.review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_edit.html')

    def test_book_list_delete_for_logged_in_user(self):
        response = self.client.get(reverse(
            'review_delete', kwargs={'pk': self.review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_delete.html')

    def add_to_wishlist_test(self):
        """ add item to wishlist and redirect to correct template"""
        response = self.client.get(reverse(
            'add_wishlist', kwargs={'pk': self.review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist_view.html')

    def test_wishlist_view(self):
        """ test for correct wishlist vioew when link is clicked"""
        response = self.client.get(reverse(
            'wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist_view.html')

    def test_wishlist_delete(self):
        """ delete item from wishlist and test for template"""
        response = self.client.get(reverse(
            'remove_wishlist', kwargs={'pk': self.wishlist.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist_delete.html')

    def test_user_delete(self):

        response = self.client.get(reverse(
            'deleteprofile', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_delete.html')

    def test_comment_create(self):
        """ create a new comment and check for destination URL"""
        response = self.client.get(reverse(
            'add_comment', kwargs={'id': self.review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_comment.html')

    def comment_update_test(self):
        """Update a comment and check for form"""
        response = self.client.get(reverse(
            'edit_comment', kwargs={'pk': self.comment.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comment_edit.html')

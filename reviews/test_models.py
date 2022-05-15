from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Review, Category, Comment, WishlistItem

class TestModels(TestCase):

    def test_item_string_method_returns_name(self):
        cat = Category.objects.create(name='Science')
        self.assertEqual(str(cat), 'Science')
    
    def test_comment_string_returns(self):
        comm = Comment.objects.create(comment_text='Here')
        self.assertEqual(str(cat), 'Here')


from django.contrib import admin
from .models import Review
from .models import Comment
from .models import Category
from .models import WishlistItem

admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(WishlistItem)



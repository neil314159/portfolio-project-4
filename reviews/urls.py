from . import views
from django.urls import path

urlpatterns = [
    path("", views.ReviewList.as_view(), name="home"),
    path('myprofile/', views.ProfileViewList.as_view(), name='myprofile'),
    path('wishlist/', views.WishlistListView.as_view(), name='wishlist'),
    path('wishlist/remove/<int:pk>', views.WishListDeleteView.as_view(), name='remove_wishlist'),
    path('wishlist/add/<int:id>', views.add_to_wishlist, name='add_wishlist'),
    path('wishlist/toggle/<int:id>', views.wishlist_toggle_read, name='toggle_wishlist'),
    path('deleteprofile/<int:pk>', views.UserDeleteView.as_view(), name='deleteprofile'),
    path('search/', views.ReviewSearchResultsListView.as_view(), name='search_results'),
    path('<slug:slug>/edit/', views.ReviewUpdateView.as_view(), name="review_edit"),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('comment/<int:pk>/edit', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('<slug:slug>/delete/', views.ReviewDeleteView.as_view(), name="review_delete"),
    path('add/', views.ReviewCreateView.as_view(), name='publish_review'),
    path('<slug:slug>/addcomment/', views.CommentCreateView.as_view(), name='add_comment'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('category/<category>', views.CategoryList.as_view(), name='category'),
    
]

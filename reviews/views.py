from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views import generic, View
from .models import Review, Comment, Category, WishlistItem
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


class ReviewList(generic.ListView):
    """ Return a listview of all reviews, ordered by date and paginated """
    model = Review
    queryset = Review.objects.order_by("-published_on")
    paginate_by = 6
    template_name = "index.html"


class ReviewDetail(generic.DetailView):
    """Class based view passing to template, form is automatically generated"""
    model = Review
    template_name = "review_detail.html"


class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    """ Create a new reviews """
    model = Review
    """ Pass in al fields except post author"""
    fields = ['title', 'book_author', 'review_text', 'category',
              'book_cover', 'purchase_link', 'star_rating']
    template_name = "review_form.html"

    def form_valid(self, form):
        """ Set the author os the post to be the currently logged in user """
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin,
                       UserPassesTestMixin, generic.UpdateView):
    """ Edit a published review """
    model = Review
    template_name = "review_edit.html"
    fields = ['title', 'book_author', 'review_text', 'category', 'book_cover',
              'purchase_link', 'star_rating']

    def test_func(self):
        """ Check that the user editing the post is creator of the post """
        obj = self.get_object()
        return obj.author == self.request.user


class ReviewDeleteView(LoginRequiredMixin,
                       UserPassesTestMixin, generic.DeleteView):
    """ Delete a review from the site"""
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('reviews')

    """ Check for ownership of review"""
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ReviewSearchResultsListView(generic.ListView):
    """ Use GET to pass in search, paginate results and pass to template"""
    model = Review
    context_object_name = 'review_list'
    template_name = 'search_results.html'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('searchterm')
        return Review.objects.filter(
            Q(title__icontains=query) | Q(review_text__icontains=query)
            )


class ProfileViewList(LoginRequiredMixin, generic.ListView):
    """ Creates view of the profile page, with reviews written by the user"""
    model = Review
    queryset = Review.objects.order_by("-published_on")
    template_name = "profile_view.html"

    def get_queryset(self):
        return Review.objects.filter(
            author=self.request.user).order_by('-published_on')


class UserDeleteView(LoginRequiredMixin,
                     UserPassesTestMixin, generic.DeleteView):
    """ Allows user to delete their own account"""
    model = User
    template_name = 'user_delete.html'
    """ Redirect to home page after"""
    success_url = reverse_lazy('home')
    success_message = "Your account has been deleted"

    def test_func(self):
        """ Check for correct permissions to delete account"""
        obj = self.get_object()
        return obj.id == self.request.user.id


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    """ Create a new comment which is attached to a review page"""
    model = Comment
    fields = ['comment_text', ]
    template_name = "add_comment.html"
    """ Redirect after successfully posting"""
    # success_url = reverse_lazy(self.object.review.get_absolute_url)
    
    
    success_url = '/'

    


    def form_valid(self, form):
        """ The author of the comment is the currently logged in user"""
        form.instance.author = self.request.user
        """ The current review is found and attached to the comment"""
        queryset = Review.objects.all()
        current_review = get_object_or_404(queryset, id=self.kwargs['id'])
        form.instance.review = current_review
        return super().form_valid(form)


class CommentDeleteView(LoginRequiredMixin,
                        UserPassesTestMixin, generic.DeleteView):
    """ Allow user to delete their own comment"""
    model = Comment
    template_name = "comment_delete.html"
    fields = ['comment_text', ]
    success_url = '/'

    def test_func(self):
        """ Check for ownership first"""
        obj = self.get_object()
        """The comment can be deleted by author or by author of the review"""
        return (obj.author == self.request.user) or (
            obj.review.author == self.request.user
            )


class CommentUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin, generic.UpdateView):
    """ Update a user comment"""
    model = Comment
    template_name = "comment_edit.html"
    fields = ['comment_text', ]
    success_url = '/'

    def test_func(self):
        """ Check for permissions first"""
        obj = self.get_object()
        return obj.author == self.request.user


class CategoryList(generic.ListView):
    """Takes GET request, returns articles by category"""
    model = Category
    template_name = "category.html"
    context_object_name = 'categorylist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'reviews': Review.objects
            .filter(category__name=self.kwargs['category'])
        }
        return content


def review_category_list(request):
    """ Creates a list of categories to be used by navbar for dropdown menu"""
    review_category_list = Category.objects.all()
    context = {"review_category_list": review_category_list, }
    return context


@login_required
def add_to_wishlist(request, id):
    """ Adds a book review to the user's wishlist"""
    """ Checks the review exists to avoid accessing nonexistent objects"""
    try:
        bookreview = Review.objects.get(id=id)
    except:
        """If not, return to the wishlist page """
        return HttpResponseRedirect(reverse_lazy('wishlist'))
    """Make sure the wishlist object does not exists already """
    if WishlistItem.objects.filter(author=request.user,
                                   review=bookreview).count() > 0:
        return HttpResponseRedirect(reverse_lazy('wishlist'))
    """ Create the wishlist item and return the user to wishlist page"""
    WishlistItem.objects.create(author=request.user, review=bookreview)
    return HttpResponseRedirect(reverse_lazy('wishlist'))


@login_required
def wishlist_toggle_read(request, id):
    """ Toggles the boolean value to show if a book is read/unread"""
    try:
        wishlist = WishlistItem.objects.get(id=id)
    except:
        return HttpResponseRedirect(reverse_lazy('wishlist'))
    wishlist.book_marked_as_read = not wishlist.book_marked_as_read
    wishlist.save()
    """ Returns to page that made request"""
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class WishlistListView(LoginRequiredMixin, generic.ListView):
    """ Creates view of wishlist page for user"""
    model = WishlistItem
    context_object_name = 'wishlist'
    template_name = 'wishlist_view.html'
    """ Return all objects belonging to user in reverse chronological order"""
    def get_queryset(self):
        return WishlistItem.objects.filter(
            author=self.request.user
            ).order_by('-published_on')


class WishListDeleteView(LoginRequiredMixin,
                         UserPassesTestMixin, generic.DeleteView):
    """ Allows deletion of wishlist items after checking for ownership"""
    model = WishlistItem
    template_name = 'wishlist_delete.html'
    success_url = reverse_lazy('wishlist')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class HomePageView(generic.TemplateView):
    template_name = 'home.html'


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
    model = Review
    queryset = Review.objects.order_by("-published_on")
    paginate_by = 2
    template_name = "index.html"


class ReviewDetail(generic.DetailView):
    model = Review
    template_name = "review_detail.html"
    # def get(self, request, slug, *args, **kwargs):
    #     queryset = Review.objects.all()
    #     review = get_object_or_404(queryset, slug=slug)
    #     return render(
    #         request,
    #         "review_detail.html",
    #         {
    #             "review": review,
    #         },
    #     )

    # def post(self, request, slug, *args, **kwargs):
    #     queryset = Review.objects.all()
    #     review = get_object_or_404(queryset, slug=slug)
    #     return render(
    #         request,
    #         "review_detail.html",
    #         {
    #             "review": review,
    #         },
    #     )

class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Review
    fields = ['title', 'review_text', 'category', 'book_cover','purchase_link', 'star_rating']
    template_name = "review_form.html"
    # success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Review
    template_name = "review_edit.html"
    fields = ['title', 'review_text', 'purchase_link', 'star_rating']
    # success_url = '/'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ReviewSearchResultsListView(generic.ListView):
    model = Review
    
    context_object_name = 'review_list'
    template_name = 'search_results.html'

    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('searchterm')
        return Review.objects.filter(
            Q(title__icontains=query) | Q(review_text__icontains=query)
            )


class ProfileViewList(LoginRequiredMixin, generic.ListView):
    model = Review
    queryset = Review.objects.order_by("-published_on")

    template_name = "profile_view.html"

    def get_queryset(self):
        return Review.objects.filter(author=self.request.user).order_by('-published_on')
    


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Your account has been deleted"

   
    def test_func(self):
       

        obj = self.get_object()
       
        return obj.id == self.request.user.id
        


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ['comment_text', ]
    template_name = "add_comment.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        queryset = Review.objects.all()
        tempreview = get_object_or_404(queryset, slug=self.kwargs['slug'])
        form.instance.review = tempreview
        return super().form_valid(form)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = "comment_delete.html"
    fields = ['comment_text', ]
    success_url = '/'

    def test_func(self):
        obj = self.get_object()
        
        

        return (obj.author == self.request.user) or (obj.review.author == self.request.user)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    template_name = "comment_edit.html"
    fields = ['comment_text',]
    success_url = '/'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CategoryList(generic.ListView):
    model = Category

    # queryset = Review.objects.order_by("-published_on")
    template_name = "category.html"
    context_object_name = 'categorylist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'reviews': Review.objects.filter(category__name=self.kwargs['category'])
        }
        return content

# 'reviews': Review.objects.filter(category__name=self.kwargs['category'])

def review_category_list(request):
    review_category_list = Category.objects.all()
    context = { "review_category_list": review_category_list,
    }
    return context

@login_required
def add_to_wishlist(request, id):
   
    # check for invalid review page if someone uses URL manipulation 
    try:
        bookreview = Review.objects.get(id=id)
    except:
        return HttpResponseRedirect(reverse_lazy('wishlist'))

    #check if wishlist item already exists before adding
    if WishlistItem.objects.filter(author=request.user, review=bookreview).count() > 0:
        return HttpResponseRedirect(reverse_lazy('wishlist'))

    WishlistItem.objects.create(author=request.user, review=bookreview)
    return HttpResponseRedirect(reverse_lazy('wishlist'))


def wishlist_toggle_read(request, id):
    # new_book = WishlistItem()
    # new_book.author = request.user
    # queryset = Review.objects.filter(id=id)
    # WishlistItem.objects.get
    # try:
    #     bookreview = Review.objects.get(id=id)
    # except:
    WishlistItem.objects.create(author=request.user, review=bookreview)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])




class WishlistListView(LoginRequiredMixin, generic.ListView):
    model = WishlistItem
   
    context_object_name = 'wishlist'
    template_name = 'wishlist_view.html'

    def get_queryset(self):
        return WishlistItem.objects.filter(author=self.request.user).order_by('-published_on')


class WishListDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = WishlistItem
    template_name = 'wishlist_delete.html'
    success_url = reverse_lazy('wishlist')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review, Comment, Category


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by("-published_on")
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

class ReviewCreateView(generic.CreateView):
    model = Review
    fields = ['title', 'author', 'review_text', 'purchase_link', 'star_rating']
    template_name = "review_form.html"
    success_url = '/'

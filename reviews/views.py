from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by("-published_on")
    template_name = "index.html"

class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.all()
        review = get_object_or_404(queryset, slug=slug)
        
        return render(
            request,
            "review_detail.html",
            {
                "review": review,
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Review.objects.all()
        review = get_object_or_404(queryset, slug=slug)
        
        return render(
            request,
            "review_detail.html",
            {
                "review": review,
            },
        )


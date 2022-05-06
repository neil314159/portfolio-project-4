from django.shortcuts import render
from django.views import generic
from .models import Review

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by("-published_on")
    template_name = "index.html"

class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.all
        review = get_object_or_404(queryset, slug=slug)
        
       

        return render(
            request,
            "review_detail.html",
            {
                "post": post,
                
                
            },
        )
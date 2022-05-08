from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from .models import Review, Comment, Category
from django.urls import reverse_lazy


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

class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Review
    fields = ['title', 'review_text', 'purchase_link', 'star_rating']
    template_name = "review_form.html"
    # success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Review
    template_name = "review_edit.html"
    fields = ['title', 'review_text', 'purchase_link', 'star_rating']
    # success_url = '/'

class ReviewDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('home')
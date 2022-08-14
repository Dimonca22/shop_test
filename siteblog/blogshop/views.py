from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class Home(ListView):
    model = Product
    template_name = 'blogshop/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Miltim lingerie'
        return context


class TopByCategory(ListView):
    template_name = 'blogshop/top.html'
    context_object_name = 'posts'
    paginate_by = 0
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


def index(request):
    return render(request, 'blogshop/index.html')


def get_category(request, slug):
    return render(request, 'blogshop/category.html')


def get_post(request, slug):
    return render(request, 'blogshop/category.html')

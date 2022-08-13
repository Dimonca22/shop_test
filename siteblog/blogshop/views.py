from django.shortcuts import render


def index(request):
    return render(request, 'blogshop/index.html')


def get_category(request, slug):
    return render(request, 'blogshop/category.html')

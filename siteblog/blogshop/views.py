from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'blogshop/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'blogshop/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


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

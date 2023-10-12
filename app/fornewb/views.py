from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, logout_then_login, login_required
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.viewsets import ModelViewSet

from .models import *
from .forms import *
from .serializers import FornewbSerializers
from .utils import *

class FornewbHome(DataMixin, ListView):
    model = Fornewb                         # тут модель вызывает коллекцию не post а object_list
    template_name = 'fornewb/index.html'
    context_object_name = 'posts'           # переменная которая в шаблоне будет применятся вместо object_list

    # Ранее у нас был список словаря menu, чтобы этот динамический словарь передать
    # используется функция ниже, но мы перенесли ее в fornewb_tags.py
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))
    # функция для того чтоб отображались только опубликованные статьи
    def get_queryset(self):
        return Fornewb.objects.filter(is_published=True)


def categories(request):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1>")


def about(request):
    return HttpResponse("О нас")

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm    # CreateView работает только с формами поэтому указываем модель через form_class
    template_name = 'fornewb/addpage.html'
    success_url = reverse_lazy('home')        # При успешном добавлении записи возвращает на домашнюю страницу (по умолчанию возвращает на добавленую статью
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))


def contact(request):
    return HttpResponse("Обратная связь")

def useraccount(request):
    return HttpResponse("Это ваша личная страничка но в ней ничего нет пока")
def logoutuser(request):
    return logout_then_login(request, login_url='login')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowPost(DataMixin, DetailView):
    model = Fornewb
    template_name = 'fornewb/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class FornewbCategory(DataMixin, ListView):
    model = Fornewb
    template_name = 'fornewb/index.html'
    context_object_name = 'posts'
    allow_empty = False           # генерирует 404 если не найдет страницу

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(article_title=str(context['posts'][0].cat) + ' для изучения статьи',
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Fornewb.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'fornewb/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save('home')
        login(self.request, user)
        #return login_required('home')
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm            # AuthenticationForm
    template_name = 'fornewb/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

# API

class FornewbViewSet(ModelViewSet):
    queryset = Fornewb.objects.all()
    serializer_class = FornewbSerializers

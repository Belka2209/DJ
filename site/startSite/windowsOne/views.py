from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class ProductHome(DataMixin, ListView):
    model = Product
    template_name = 'windowsOne/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Product.objects.filter().select_related('cat')
# def index(request):
#     posts = Product.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#
#     }
#     return render(request, 'windowsOne/index.html', context=context)

# @login_required
def about(request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'windowsOne/about.html', {'page_obj': page_obj, 'menu': menu, 'title': "О сайте"})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'windowsOne/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True       #страница 403 доступ запрещен


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление курса')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             #print(form.cleaned_data)
#
#                 form.save()
#                 return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'windowsOne/addpage.html', {'form': form,  'menu': menu, 'title': 'Добавление курса'})


# def contact(request):
#     return HttpResponse("<h1>Обратная связь</h1>")

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'windowsOne/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


# def login(request):
#     return HttpResponse("<h1>Авторизация</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowPost(DataMixin, DeleteView):
    model = Product
    template_name = 'windowsOne/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Product, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.name,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'windowsOne/post.html', context=context)
#

class ProductCategory(DataMixin, ListView):
    model = Product
    template_name = 'windowsOne/index.html'
    context_object_name = 'posts'
    allow_empty = False



    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['cat_slug'])



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0]), cat_selected=context['posts'][0].cat_id)
        context = dict(list(context.items()) + list(c_def.items()))
        return context



# def show_category(request, cat_id):
#     posts = Product.objects.all()
#
#
#     if len(posts) == 0:
#         raise Http404()
#
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#
#     }
#     return render(request, 'windowsOne/index.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'windowsOne/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, odjects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'windowsOne/login.html'

    def get_context_data(self, *, odjects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')



class RegisterZaivkaUser(DataMixin, FormView):
    form_class = SetUserForm
    template_name = 'windowsOne/z_user.html'
    success_url = reverse_lazy('home')
    context_object_name = 'qwe'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Запись на курс')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


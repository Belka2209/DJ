from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *
# с функцией кэширования path('', cache_page(60)(ProductHome.as_view()), name='home'),
urlpatterns = [
    path('', ProductHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('qwe/', RegisterZaivkaUser.as_view(), name='qwe'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ProductCategory.as_view(), name='category'),


]
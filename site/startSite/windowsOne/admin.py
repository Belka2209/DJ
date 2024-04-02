from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'price', 'content', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price', 'photo')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'cat', 'price', "dataStart", 'data_end', 'content', 'photo', 'group_min_participants', 'group_man_participants' )
    save_on_top = True

    def get_html_photo(self, object):    #  Для отображения картинки продукта в админ панели
        if object.photo:
            return mark_safe(f"<img scr='{object.photo.url}' width=50")

    get_html_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель сайта о курсах'
admin.site.site_header = 'Админ-панель сайта о курсах 2'
# Register your models here.

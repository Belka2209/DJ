from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse




class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Наименование курса")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    dataStart = models.DateTimeField('Время начала')
    data_end = models.DateTimeField('Время конца')
    price = models.IntegerField(default=0, verbose_name='Цена')
    group_min_participants = models.PositiveIntegerField(verbose_name="Минимальное числов в группе")
    group_man_participants = models.IntegerField(verbose_name='Максимальное числов в группе')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    content = models.TextField(blank=True, verbose_name="Описание курса")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'
        ordering = ['id']



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id' ]



    def get_absolute_url(self):
        return reverse("category", kwargs={'cat_slug': self.slug})


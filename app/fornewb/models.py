from django.db import models
from django.urls import reverse

class Fornewb(models.Model):
    article_title = models.CharField(max_length=255, verbose_name='Название статьи')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Содержание статьи')
    photo = models.ImageField(upload_to="article_image/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликована ли')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.article_title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Статьи для новичков программистов"         # как будет отображатся в админке в одиночном числе
        verbose_name_plural = "Статьи для новичков программистов"  # как будет отображатся в админке во множественном числе
        ordering = ['-time_create', 'article_title']               # по каким полям будет сортировка


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Уровень')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Уровень сложности"
        verbose_name_plural = "Уровни сложности"
        ordering = ['name']



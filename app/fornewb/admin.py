from django.contrib import admin
from .models import *


class FornewbAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'article_title', 'photo', 'time_create')  # поля которые хотим видеть в нашей админпанели
    list_display_links = ('id', 'article_title')                                    # поля на которые кликнув перейдем в приветствующей статье
    search_fields = ('article_title', 'content')                                    # поля по которым будет поиск
    prepopulated_fields = {"slug": ("article_title",)}

admin.site.register(Fornewb, FornewbAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}     # этот параметр позволяет автоматически заполнять слаги по полю name

admin.site.register(Category, CategoryAdmin)
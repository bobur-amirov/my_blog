from django.contrib import admin

from . import models


@admin.register(models.MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio', 'img']
    search_fields = ['username', 'first_name', 'last_name']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'img']
    search_fields = ['name', 'description']


@admin.register(models.Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'description']

class CommentInline(admin.StackedInline):
    model = models.Comment

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = ['id', 'title', 'created_at', 'updated_at', 'category', 'author', 'views']
    search_fields = ['title', 'description']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'user', 'text']
    search_fields = ['blog', 'text']

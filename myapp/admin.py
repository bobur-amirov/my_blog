from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username', 'location', 'birth_date', 'bio']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'location', 'birth_date', 'img')}),
    )  # this will allow to change these fields in admin module


admin.site.register(MyUser, MyUserAdmin)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'img']
    search_fields = ['name', 'description']


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

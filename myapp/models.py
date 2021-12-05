from django.contrib.auth.models import AbstractUser
from django.db import models
from django_quill.fields import QuillField
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='category/')
    description = models.TextField()

    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    bio = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    img = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.username



class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='blogs/')
    description = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

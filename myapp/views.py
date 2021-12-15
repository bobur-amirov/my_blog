from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from taggit.models import Tag

from .forms import MyUserCreationForm, MyUserChangeForm, BlogForm
from .models import MyUser, Category, Blog, Comment


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileUpdateView(UpdateView):
    model = MyUser
    form_class = MyUserChangeForm
    success_url = reverse_lazy('blog_list')
    template_name = 'update_profile.html'


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class CategoryListView(TagMixin, ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs_top'] = Blog.objects.all().order_by('-views')
        return context


class CategoryDetailView(TagMixin, DetailView):
    model = Category
    template_name = 'category_blog.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['blogs'] = Blog.objects.filter(category__slug=slug)
        context['blog_count'] = Blog.objects.filter(category__slug=slug).count()
        context['categories'] = Category.objects.all()
        context['blogs_top'] = Blog.objects.filter(category__slug=slug).order_by('-views')
        return context


class BlogListView(TagMixin, ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_counts'] = Blog.objects.count()
        context['categories'] = Category.objects.all()
        context['blogs_top'] = Blog.objects.all().order_by('-views')
        return context


class TagView(BlogListView):

    def get_queryset(self):
        return Blog.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


def blog_detail_view(request, slug):
    blog = Blog.objects.get(slug=slug)
    blogs_author = Blog.objects.filter(author=blog.author)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        Comment.objects.create(
            blog=Blog.objects.get(title=blog.title),
            user=MyUser.objects.get(username=request.user.username),
            text=request.POST.get('comment_text')
        )
    blog.views += 1
    blog.save()
    contecxt = {
        'blog': blog,
        'categories': categories,
        'blogs_author': blogs_author,
        'tags': tags,
    }
    return render(request, 'blog_detail.html', contecxt)


class BlogCreate(CreateView):
    form_class = BlogForm
    template_name = 'blog_create.html'
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class BlogUpdate(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_update.html'
    success_url = reverse_lazy('blog_list')

class BlogDelete(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')



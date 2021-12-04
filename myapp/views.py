from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser, Category, Tags, Blog, Comment


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileUpdateView(UpdateView):
    model = MyUser
    form_class = MyUserChangeForm
    success_url = reverse_lazy('blog_list')
    template_name = 'update_profile.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_blog.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['blogs'] = Blog.objects.filter(category_id=pk)
        context['blog_count'] = Blog.objects.filter(category_id=pk).count()
        context['categories'] = Category.objects.all()
        return context


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_counts'] = Blog.objects.count()
        context['categories'] = Category.objects.all()
        return context


# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'blog_detail.html'
#     context_object_name = 'blog'

# def get_context_data(self, **kwargs):
#     context = super(BlogDetailView, self).get_context_data(**kwargs)
#     comment_form = CommentCreateView()
#     context['comment_form'] = comment_form
#     print(context['comment_form'])
#     return context


# def get_object(self, queryset=None):
#     blog_obj = super().get_object()
#     blog_obj.views += 1
#     blog_obj.save()
#     return blog_obj


def blog_detail_view(request, pk):
    blog = Blog.objects.get(id=pk)
    categories = Category.objects.all()
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
    }
    return render(request, 'blog_detail.html', contecxt)

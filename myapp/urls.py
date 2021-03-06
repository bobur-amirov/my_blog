from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile-update/<int:pk>', views.ProfileUpdateView.as_view(), name='profile_update'),

    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('create/', views.BlogCreate.as_view(), name='blog_create'),
    path('blog/<slug:slug>/edit', views.BlogUpdate.as_view(), name='blog_update'),
    path('blog/<slug:slug>/delete', views.BlogDelete.as_view(), name='blog_delete'),
    path('blog/<slug:slug>', views.blog_detail_view, name='blog_detail'),
    path('tags/<slug:tag_slug>', views.TagView.as_view(), name='blog_tags'),
]

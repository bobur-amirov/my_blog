from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>', views.blog_detail_view, name='blog_detail'),
]

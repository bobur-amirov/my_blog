from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile-update/<int:pk>', views.ProfileUpdateView.as_view(), name='profile_update'),

    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>', views.blog_detail_view, name='blog_detail'),
]

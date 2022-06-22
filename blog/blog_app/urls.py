from django.urls import path
from . import views

app_name = "blog_app"

urlpatterns = [
    path('create/', views.create_blog_post.as_view(), name='create'),
    path('view/<int:pk>/', views.view_blog_post.as_view(), name='view'),
    path('all_posts/', views.all_blog_posts.as_view(), name='all'),
    path('delete/<int:id>/', views.delet_blog_post, name='delete'),
]

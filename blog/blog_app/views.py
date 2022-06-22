from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Blog_Post
import logging

User = get_user_model()


class create_blog_post(generic.CreateView):
    model = Blog_Post
    template_name = 'blog_app/creat_post.html'
    fields = ('post_title', 'blog_content')
    success_url = reverse_lazy('blog_app:all')


class view_blog_post(generic.DetailView):
    model = Blog_Post
    template_name = 'blog_app/view_post.html'



def delet_blog_post(request, id):
    blog_post = Blog_Post.objects.get(id=id)
    blog_post.delete()
    return redirect("/")


class all_blog_posts(generic.ListView):
    model = Blog_Post
    template_name = 'blog_app/all_posts.html'
    #slug_url_kwarg = "slug"

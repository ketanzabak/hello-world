from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class PostsView(ListView):
	model = Post
	template_name = 'posts.html'

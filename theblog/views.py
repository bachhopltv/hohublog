from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	



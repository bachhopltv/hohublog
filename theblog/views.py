from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

def home_list_view(request):
	queryset = Post.objects.all() # list of objects
	context_name = {
		"object_list": queryset
	}
	return render(request, "home.html", context_name)
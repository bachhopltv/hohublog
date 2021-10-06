from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView
from .models import Post

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(queryset=Post.objects.all()), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
]

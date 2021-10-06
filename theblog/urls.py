from django.urls import path
#from . import views
from .views import HomeView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/edit/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]

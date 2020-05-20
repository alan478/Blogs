from django.urls import path
from . import views
from user import views as user_views 

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about')
]

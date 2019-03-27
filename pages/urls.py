from django.conf.urls import re_path

from django.urls import path, include
from . import views

# wait i will see



urlpatterns = [
    path('home/', views.HomePageView.as_view(), name = 'home'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    path('post/', views.post, name = 'post'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
]


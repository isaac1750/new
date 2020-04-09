from django.urls import path, include
from django.conf.urls import re_path
from . import views


urlpatterns = [
#now go to browser
    path('/contact/', views.contact_us, name='contact_us'), 

]
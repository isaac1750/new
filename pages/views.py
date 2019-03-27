from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
# Create your views here.from django.views.generic import TemplateView



class HomePageView(TemplateView):
	template_name = "home.html"



class AboutPageView(TemplateView):
	template_name = "about.html"


def post(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post.html', {'posts': posts})



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

# Create your views here.


# Create your views here.

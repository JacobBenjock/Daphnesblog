from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

posts = [
    {
    'author': 'DaphneB',
    'title': 'world of diphne',
    'content': 'first post content',
    'date_posted': 'August of 2019'
    },
    {
    'author': 'JacobB',
    'title': 'Blog post 2',
    'content': 'second post content',
    'date_posted': 'August of 2019'
    },
]

def home (request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about (request):
    return render(request, 'blog/about.html', { 'title': 'About'})

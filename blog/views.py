from django.shortcuts import render
from .models import Category, Post
# Create your views here.
def index(request):
    posts = Post.objects.filter(is_active=True).order_by('-id')
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)
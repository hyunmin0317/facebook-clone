from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.order_by('-create_date')
    context = {'posts' : posts}
    return render(request, 'facebook/home.html', context)
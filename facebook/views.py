from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.order_by('-create_date')
    context = {'posts' : posts}
    return render(request, 'facebook/home.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'facebook/post_form.html', context)
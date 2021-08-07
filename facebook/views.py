from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User

from common.models import Profile
from .models import Post, Comment
from .forms import PostForm, CommentForm

def home(request):
    posts = Post.objects.order_by('-create_date')
    context = {'posts' : posts}
    return render(request, 'facebook/home.html', context)

def post_user(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    posts = Post.objects.filter(author=user)
    context = {'users' : user, 'posts' : posts, 'profile' : profile}
    return render(request, 'facebook/post_user.html', context)

@login_required(login_url='common:login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.save()
            return redirect('facebook:post_user', username=post.author.username)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'facebook/post_form.html', context)

@login_required(login_url='common:login')
def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('facebook:post_user', username=post.author.username)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modify_date = timezone.now()  # 수정일시 저장
            post.save()
            return redirect('facebook:post_user', username=post.author.username)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'facebook/post_form.html', context)

@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('facebook:post_user', username=post.author.username)
    post.delete()
    return redirect('facebook:post_user', username=post.author.username)

@login_required(login_url='common:login')
def comment_create_post(request, post_id, before):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.post = post
            comment.save()
            if(before=='home'):
                return redirect('home')
            return redirect('facebook:post_user', post.author.username)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'facebook/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_post(request, comment_id, before):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('home')

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            if (before == 'home'):
                return redirect('home')
            return redirect('facebook:post_user', comment.post.author.username)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'facebook/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_post(request, comment_id, before):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
    else:
        comment.delete()
    if (before == 'home'):
        return redirect('home')
    return redirect('facebook:post_user', comment.post.author.username)

@login_required(login_url='common:login')
def vote_post(request, post_id, before):
    post = get_object_or_404(Post, pk=post_id)
    post.voter.add(request.user)
    if(before=='home'):
        return redirect('home')
    return redirect('facebook:post_user', post.author.username)

def follow(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'facebook/follow.html', context)

@login_required(login_url='common:login')
def following(request, username):
    profile = get_object_or_404(Profile, user=request.user)
    user = get_object_or_404(User, username=username)
    profile.follow.add(user)
    return redirect('home')
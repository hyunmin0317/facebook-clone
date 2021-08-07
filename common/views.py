from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile


# 계정생성
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        forms = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증

            profile = forms.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)  # 로그인
            return redirect('home')
    else:
        form = UserForm()
        forms = ProfileForm()
    context = {'form': form, 'forms': forms}
    return render(request, 'common/signup.html', context)

@login_required(login_url='common:login')
def modify(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    if request.user != user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('facebook:post_user', username=username)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('facebook:post_user', username=username)
        
    else:
        form = ProfileForm(instance=profile)
    context = {'form': form}
    return render(request, 'common/modify.html', context)
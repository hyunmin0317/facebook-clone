from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm, ProfileForm
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
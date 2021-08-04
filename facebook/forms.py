from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post    # 사용할 모델
        fields = ['title', 'image', 'content']     # PostForm에서 사용할 Post 모델의 속성
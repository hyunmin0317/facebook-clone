from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post    # 사용할 모델
        fields = ['title', 'image', 'content']     # PostForm에서 사용할 Post 모델의 속성

        labels = {
            'title': '제목',
            'image': '이미지',
            'content': '내용',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'rows': 10}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
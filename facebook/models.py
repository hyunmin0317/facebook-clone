from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from common.models import Profile

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, blank=True, related_name='voter_post')

    def __str__(self):
        return self.title

    def profile(self):
        profile = get_object_or_404(Profile, user=self.author)
        return profile

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
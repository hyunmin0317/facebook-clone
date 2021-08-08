from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    follow = models.ManyToManyField(User, blank=True, related_name='follow')
    follower = models.ManyToManyField(User, blank=True, related_name='follower')

    def __str__(self):
        return self.user.username
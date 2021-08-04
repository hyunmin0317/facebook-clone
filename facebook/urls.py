from django.urls import path
from . import views

app_name='facebook'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.post_create, name='post_create')
]
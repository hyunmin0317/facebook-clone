from django.urls import path
from . import views

app_name='facebook'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<str:username>/', views.post_user, name='post_user'),
    path('post/modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('comment/create/post/<int:post_id>/<str:before>/', views.comment_create_post, name='comment_create_post'),
    path('comment/modify/question/<int:comment_id>/<str:before>/', views.comment_modify_post, name='comment_modify_post'),
    path('comment/delete/question/<int:comment_id>/<str:before>/', views.comment_delete_post, name='comment_delete_post'),
    path('vote/post/<int:post_id>/<str:before>/', views.vote_post, name='vote_post'),
    path('follow/', views.follow, name='follow'),
    path('follow/<str:username>/', views.following, name='following'),
    path('unfollow/<str:username>/', views.unfollowing, name='unfollowing'),
    path('follow/all/<str:username>/', views.follow_all, name='follow_all'),
    path('follower/all/<str:username>/', views.follower_all, name='follower_all'),
]
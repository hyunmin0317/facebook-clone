from django.urls import path
from . import views

app_name='facebook'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:username>/', views.post_user, name='post_user'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('comment/create/post/<int:post_id>/<str:before>/', views.comment_create_post, name='comment_create_post'),
    path('comment/modify/question/<int:comment_id>/<str:before>/', views.comment_modify_post, name='comment_modify_post'),
    path('comment/delete/question/<int:comment_id>/<str:before>/', views.comment_delete_post, name='comment_delete_post'),
    path('vote/post/<int:post_id>/<str:before>/', views.vote_post, name='vote_post'),
]
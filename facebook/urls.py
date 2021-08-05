from django.urls import path
from . import views

app_name='facebook'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.post_create, name='post_create'),
    path('comment/create/post/<int:post_id>/', views.comment_create_post, name='comment_create_post'),
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_post, name='comment_modify_post'),
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_post, name='comment_delete_post'),
    path('vote/post/<int:post_id>/', views.vote_post, name='vote_post'),
]
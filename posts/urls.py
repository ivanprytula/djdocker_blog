from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('new/', login_required(views.PostNew.as_view()), name='post_new'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

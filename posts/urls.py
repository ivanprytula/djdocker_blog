from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'posts'

urlpatterns = [
    path('', login_required(views.PostList.as_view()), name='post_list'),
    # path('', views.PostList.as_view(), name='post_list'),
]

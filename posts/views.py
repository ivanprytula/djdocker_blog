from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from .models import Post
from .forms import PostForm


class PostList(generic.ListView):
    context_object_name = 'filtered_post_list'
    queryset = Post.objects.filter(created_date__lte=timezone.now())
    template_name = 'posts/post_list.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class PostNew(generic.CreateView):
    form_class = PostForm

    template_name = 'posts/post_new.html'
    success_url = '/posts/'

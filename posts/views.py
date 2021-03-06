from django.utils import timezone
from django.views import generic

from .forms import PostForm
from .models import Post


class PostList(generic.ListView):
    context_object_name = 'filtered_post_list'
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class PostNew(generic.CreateView):
    form_class = PostForm

    template_name = 'posts/post_new.html'
    success_url = '/posts/'

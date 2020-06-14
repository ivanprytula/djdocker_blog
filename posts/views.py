from django.utils import timezone
from django.views import generic

from .models import Post


class PostList(generic.ListView):
    context_object_name = 'filtered_post_list'
    queryset = Post.objects.filter(published_date__lte=timezone.now())
    template_name = 'posts/post_list.html'


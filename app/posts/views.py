from django.shortcuts import render
from .models import Posts
import pprint

# Create your views here.
def posts_list(request):
    posts = Posts.objects.all()
    # pprint(vars(posts))
    # die
    data = {
        'posts': posts
    }
    return render(request, 'posts/list.html', context=data)


def create(request):
    data = {}
    return render(request, 'posts/create.html', context=data)    
from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm

# Create your views here.
def posts_list(request):
    # posts = Posts.objects.all() # вывести все записи
    posts = Posts.objects.order_by('-date_public') # сортировать по дате
    # pprint(vars(posts))
    # die
    data = {
        'posts': posts
    }
    return render(request, 'posts/list.html', context=data)


def create(request):
    errors = ''
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
        else:
            errors = form.errors
    else:
        form = PostsForm()

    data = {
        'form': form,
        'errors': errors,
    }
    return render(request, 'posts/create.html', context=data)    
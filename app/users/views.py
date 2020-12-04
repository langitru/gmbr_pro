from django.shortcuts import render

# Create your views here.
def users_list(request):
    content = {
        
    }
    return render(request, 'users/list.html', context=content)


def user_profile(request):

    return render(request, 'users/profile.html', context = {})
from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        
    }
    return render(request, 'main/home.html', context=content)
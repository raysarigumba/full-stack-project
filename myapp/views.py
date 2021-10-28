from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World! This is the index page.')
def my_name(request):
    context = {'name': 'Ray Ivan Sarigumba'}
    return render(request, 'myapp/myapp.html', context)
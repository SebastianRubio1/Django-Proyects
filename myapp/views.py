from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import project, Task


def index( request ):
    return HttpResponse("<h1>Index Page</h1>")

def hello( request, username ):
    print(username)
    return HttpResponse('Hello %s' % username)

def about( request ):
    return HttpResponse('<h1>About us</h1>')

def products( request ):
    return HttpResponse('<h1>Products</h1>')

def operacion (request, number):
    result=(number+100)*2
    return HttpResponse('<h1>El resultado de (%s + 100) * 2 es %s</h1>' % (number, result))


def projects(request):
    projects= list(project.objects.values())
    return JsonResponse(projects, safe=False)

def Task(request):
    return HttpResponse("<h1>Tasks</h1>")
        

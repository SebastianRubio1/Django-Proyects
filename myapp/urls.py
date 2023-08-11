from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('hello/<str:username>',views.hello),
    path('operacion/<int:number>',views.operacion),
    path('projects', views.projects),
    path('Task', views.Task),
]


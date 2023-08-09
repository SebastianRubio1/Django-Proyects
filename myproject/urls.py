
from django.contrib import admin
from django.urls import path,include
from myapp.views import hello,about,products
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('about', about),
    path('products', products),
    path('',include('myapp.urls')),
]

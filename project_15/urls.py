from django.contrib import admin
from django.urls import path
from project_15.views import home, login, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', home),
    path('login/', login),
    path('index/', index),
]

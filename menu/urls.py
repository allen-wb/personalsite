from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('get_menus', views.get_menus, name='get_menus'),
]

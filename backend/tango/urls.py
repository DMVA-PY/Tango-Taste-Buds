from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('messi', views.messi, name='messi'),
    path('breakfast', views.breakfast, name='breakfast'),
    path('lunch', views.lunch, name='lunch'),
    path('dinner', views.dinner, name='dinner'),
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.sucursalacompañamientos_view, name='sucursalacompañamientos_view'),
    path('<int:pk>', views.sucursalacompañamiento_view, name='sucursalacompañamiento_view'),
]
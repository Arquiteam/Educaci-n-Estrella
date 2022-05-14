from django.urls import path
from . import views
urlpatterns = [
    path('', views.estudiantes_view, name='estudiantes_view'),
    path('<str:pk>', views.estudiante_view, name='estudiante_view'),
]
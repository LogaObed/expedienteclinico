from django.urls import path
from paciente import views
urlpatterns = [
    path('ver/',views.paciente,name='paciente')
]
from django.urls import path
from paciente import views
urlpatterns = [
    path('',views.inicio,name='paciente'),
    path('registro-general/',views.formGeneral,name='verpaciente'),
    path('consulta/',views.consultaPacientes,name='consultapaciente'),
    path('consulta-ajax/',views.consultaPacientesajax ,name='consultapacienteajax'),
    path('nuevo/', views.nuevoPaciente,name='nuevopaciente'),
    path('editar/<int:dato>', views.editarPaciente,name='editarpaciente'),
]
from django.urls import path
from paciente import views
urlpatterns = [
    path('',views.inicio,name='paciente'),
    path('registro-general/',views.formGeneral,name='verpaciente'),
    path('consulta/',views.consultaPacientes,name='consultapaciente'),
    path('consulta-ajax/',views.consultaPacientesajax ,name='consultapacienteajax'),
    path('nuevo/', views.nuevoPaciente,name='nuevopaciente'),
    path('editar/<int:dato>', views.editarPaciente,name='editarpaciente'),
    path('editar/paciente/<int:dato>', views.editarPacienteAjax,name='editarpacienteajax'),
    path('editar-preferencia/<int:prefe>', views.editarPreferencia,name='editarprefe'),
    path('editar-datos-generales/<int:datogeneral>', views.editarDatoGeneral,name='editardatogeneral'),
    path('editar-heredo-familiar/<int:heredofamiliar>', views.editarHeredoFamiliar,name='editarheredofamiliar'),
    path('editar-patologias/<int:patologico>', views.editarPatologicos,name='editarpatologicos'),
    path('editar-no-patologias/<int:patologico>', views.editarNoPatologicos,name='editarnopatologicos'),
    path('editar-habitos-alimenticios/<int:habito>', views.editaHalimenticio,name='editaralimenticio'),
    path('editar-exploracion/<int:exploracion>', views.editaExploracion,name='editarexploracion'),
    path('editar-sangre/<int:sangre>', views.edtirarSangre,name='editarsangre'),
    path('editar-sexo/<int:sexo>', views.edtirarSexo,name='editarsexo'),
    path('editar-notas/<int:notas>', views.edtirarNotas,name='editarnotas'),
]
from django.contrib import admin
from paciente.models import *
admin.site.register(TipoUsuario)
admin.site.register(TipoSangre)
admin.site.register(TipoSexo)
admin.site.register(Paciente)
admin.site.register(DatosGeneral)
admin.site.register(Preferencia)
admin.site.register(NotaPaciente)
admin.site.register(AntecedentePersonal)
admin.site.register(AntecedenteFamiliar)
admin.site.register(AntecedentePatologico)
admin.site.register(AntecedenteAlimenticio)
admin.site.register(Exploracion)
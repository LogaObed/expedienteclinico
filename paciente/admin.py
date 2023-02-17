from django.contrib import admin
from paciente.models import *
admin.site.register(TipoUsuario)
admin.site.register(TipoSangre)
admin.site.register(TipoSexo)
admin.site.register(Paciente)
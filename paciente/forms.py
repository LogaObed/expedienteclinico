from django.forms import *
from paciente.models import *


class FormNuevoPaciente(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'telefono', 'email',
                  'tipo_usuario', 'tipo_sangre', 'tipo_sexo']
        widgets = {
            'tipo_usuario': TextInput(attrs={'type': 'hidden', 'value': 2}),
            'tipo_sangre': TextInput(attrs={'type': 'hidden', 'value': 1}),
            'tipo_sexo': TextInput(attrs={'type': 'hidden', 'value': 1}),
        }


class FormPacienteGeneral(ModelForm):
    class Meta:
        model = DatosGeneral
        fields = ['fecha_nacimiento', 'telefono', 'celular', 'domicilio', 'ciudad', 'estado',
                  'cp', 'lugar_nacimiento', 'ocupacion', 'region', 'clave_app', 'datofiscal']
        widgets = {
            'fecha_nacimiento': DateInput(attrs={'type': 'date'}),
        }


class FormPreferencia(ModelForm):
    class Meta:
        model = Preferencia
        fields = ['nombre_pareja', 'fecha_aniversario', 'nombre_hijos', 'fecha_hijo', 'nombre_empresa',
                  'fecha_empresa', 'deportes', 'pelicula_serie', 'musica', 'vehiculo', 'comida']
        widgets = {
            'fecha_aniversario': DateInput(attrs={'type': 'date'}),
            'fecha_hijo': DateInput(attrs={'type': 'date'}),
            'fecha_empresa': DateInput(attrs={'type': 'date'}),
        }

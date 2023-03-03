from django.forms import *
from paciente.models import *
from crispy_forms.layout import Layout, Div, Field


class FormNuevoPaciente(ModelForm):
    class Meta:
        model = Paciente
        exclude = ['empresa', 'foto']
        widgets = {
            'tipo_usuario': TextInput(attrs={'type': 'hidden', 'value': 2}),
            'tipo_sangre': TextInput(attrs={'type': 'hidden', 'value': 1}),
            'tipo_sexo': TextInput(attrs={'type': 'hidden', 'value': 1}),
        }


class FormPacienteGeneral(ModelForm):
    class Meta:
        model = DatosGeneral
        exclude = ['propietario']
        widgets = {
            'domicilio': TextInput(attrs={'onblur': 'guardardatosgenerales();', 'class': 'form-control form-control-sm text-left', 'placeholder': 'Domicilio', 'data-placement': 'left'}),
            'ciudad': TextInput(attrs={'onblur': 'guardardatosgenerales();', 'class': 'form-control form-control-sm text-left', 'placeholder': 'Ciudad', 'data-placement': 'left'}),
            'estado': TextInput(attrs={'onblur': 'guardardatosgenerales();', 'class': 'form-control form-control-sm text-left', 'placeholder': 'Estado', 'data-placement': 'left'}),
            'lugar_nacimiento': TextInput(attrs={'onblur': 'guardardatosgenerales();', 'class': 'form-control form-control-sm text-left', 'placeholder': 'Lugar de Nacimiento', 'data-placement': 'left'}),
            'ocupacion': TextInput(attrs={'onblur': 'guardardatosgenerales();', 'class': 'form-control form-control-sm text-left', 'placeholder': 'Ocupación', 'data-placement': 'left'}),
            'region': TextInput(attrs={'onblur': 'guardardatosgenerales();', 'class': 'form-control form-control-sm text-left', 'placeholder': 'Religión', 'data-placement': 'left'}),
            'clave_app': TextInput(attrs={'onblur': 'guardardatosgenerales();', 'class': 'form-control form-control-sm text-left', 'placeholder': 'Clave de la APP', 'data-placement': 'left'}),
            'cp': NumberInput(attrs={'min':'0','onblur': 'guardardatosgenerales();', 'class': 'form-control form-control-sm text-left', 'placeholder': 'Código Postal', 'data-placement': 'left'}),
            'celular': NumberInput(attrs={'type': 'tel', 'onblur': 'guardardatosgenerales();', 'class': 'form-control form-control-sm text-left', 'placeholder': 'Teléfono Celular', 'data-placement': 'left'}),
            'telefono': NumberInput(attrs={'type': 'tel', 'onblur': 'guardardatosgenerales();', 'class': 'form-control form-control-sm text-left', 'placeholder': 'Teléfono Principal', 'data-placement': 'left'}),
        }


class FormPreferencia(ModelForm):
    class Meta:
        model = Preferencia
        exclude = ['propietario']
        widgets = {
            'experiencia': Textarea(attrs={'class': 'form-control form-control-sm', 'rows': '4', 'onblur': 'guardarprefe();'}),
            'nombre_pareja': TextInput(attrs={'type': 'text', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
            'fecha_aniversario': DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm', 'onblur': 'guardarprefe();'}),
            'nombre_hijos': TextInput(attrs={'type': 'text', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
            'fecha_hijo': DateInput(attrs={'type': 'date', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
            'nombre_empresa': TextInput(attrs={'type': 'text', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
            'fecha_empresa': DateInput(attrs={'type': 'date', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
            'gustos': TextInput(attrs={'type': 'text', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
            'pelicula_serie': TextInput(attrs={'type': 'text', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
            'musica': TextInput(attrs={'type': 'text', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
            'deportes': TextInput(attrs={'type': 'text', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
            'comida': TextInput(attrs={'type': 'text', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
            'vehiculo': TextInput(attrs={'type': 'text', 'onblur': 'guardarprefe();', 'class': 'form-control form-control-sm'}),
        }


class FormNota(ModelForm):
    class Meta:
        model = NotaPaciente
        exclude = ['propietario']


class FormAntecedenteFamiliar(ModelForm):
    class Meta:
        exclude = ['propietario']
        model = AntecedenteFamiliar
        widgets = {
            'hermanos': NumberInput(attrs={'min':'0','class':'form-control form-control-sm text-center','onblur':'guardarheredofamiliar();','data-placement':'left'}),
            'diabetes': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'hip_arterial': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'cardiopatias': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'hepatopatias': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'urologicos': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'neurologicos': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'respiratorios': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'cancer': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'alergias': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'metabolicas': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'sanguineas': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'articulares': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'inmunologicas': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'malformaciones': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'dermatologicas': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),
            'otros': TextInput(attrs={'onblur': 'guardarheredofamiliar();', 'class': 'form-control form-control-sm text-center'}),

        }


class FormAntecedentePersonal(ModelForm):
    class Meta:
        model = AntecedentePersonal
        exclude = ['propietario']
        widgets = {
            'ultima_desparacita': DateInput(attrs={'type': 'date'}),
        }


class FormAntecedentePatologico(ModelForm):
    class Meta:
        model = AntecedentePatologico
        exclude = ['propietario']


class FormAntecedenteAlimenticio(ModelForm):
    class Meta:
        model = AntecedenteAlimenticio
        exclude = ['propietario']
        # fields = '__all__'


class FormExploracion(ModelForm):
    class Meta:
        model = Exploracion
        exclude = ['propietario']

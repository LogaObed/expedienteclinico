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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'autocomplete': 'off', 'onblur': 'guardardatosgenerales();', 'onchange': 'guardardatosgenerales();',
                                           'class': 'form-control form-control-sm text-left', 'data-toggle': 'tooltip', 'data-placement': 'left'})

    class Meta:
        model = DatosGeneral
        exclude = ['propietario']
        widgets = {
            'domicilio': TextInput(attrs={'placeholder': 'Domicilio', 'title': 'Domicilio'}),
            'ciudad': TextInput(attrs={'placeholder': 'Ciudad', 'title': 'Ciudad'}),
            'estado': TextInput(attrs={'placeholder': 'Estado', 'title': 'Estado'}),
            'lugar_nacimiento': TextInput(attrs={'placeholder': 'Lugar de Nacimiento', 'title': 'Lugar de Nacimiento'}),
            'ocupacion': TextInput(attrs={'placeholder': 'Ocupación', 'title': 'Ocupación'}),
            'region': TextInput(attrs={'placeholder': 'Religión', 'title': 'Religión'}),
            'clave_app': TextInput(attrs={'placeholder': 'Clave de la APP', 'title': 'Clave de la APP'}),
            'cp': NumberInput(attrs={'min': '0', 'placeholder': 'Código Postal', 'title': 'Código Postal'}),
            'celular': NumberInput(attrs={'type': 'tel', 'placeholder': 'Teléfono primario', 'title': 'Teléfono primario'}),
            'telefono': NumberInput(attrs={'type': 'tel', 'placeholder': 'Teléfono secundario', 'title': 'Teléfono secundario'}),
        }


class FormPreferencia(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'autocomplete': 'off', 'onblur': 'guardarprefe();', 'onchange': 'guardarprefe();',
                                           'class': 'form-control form-control-sm text-left', 'data-toggle': 'tooltip', 'data-placement': 'left'})

    class Meta:
        model = Preferencia
        exclude = ['propietario']
        widgets = {
            'experiencia': Textarea(attrs={'rows': '4', 'placeholder': 'Experiencia...', 'title': 'Experiencia'}),
            'nombre_pareja': TextInput(attrs={'title': 'Nombre de Pareja', 'placeholder': 'Nombre de Pareja...', }),
            'fecha_aniversario': DateInput(attrs={'type': 'date'}),
            'nombre_hijos': TextInput(attrs={'title': 'Hijo', 'placeholder': 'Hijo...', }),
            'fecha_hijo': DateInput(attrs={'type': 'date'}),
            'nombre_empresa': TextInput(attrs={'title': 'Empresa', 'placeholder': 'Empresa...', }),
            'fecha_empresa': DateInput(attrs={'type': 'date'}),
            'gustos': TextInput(attrs={'title': 'Gustos y Preferencias', 'placeholder': 'Gustos y Preferencias...', }),
            'pelicula_serie': TextInput(attrs={'title': 'Series y Películas', 'placeholder': 'Series y Películas...', }),
            'musica': TextInput(attrs={'title': 'Música', 'placeholder': 'Música...', }),
            'deportes': TextInput(attrs={'title': 'Deportes', 'placeholder': 'Deportes...', }),
            'comida': TextInput(attrs={'title': 'Comida', 'placeholder': 'Comida...', }),
            'vehiculo': TextInput(attrs={'title': 'Vehículos', 'placeholder': 'Vehículos...', }),
        }


class FormNota(ModelForm):
    class Meta:
        model = NotaPaciente
        exclude = ['propietario']


class FormAntecedenteFamiliar(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update(
                {'autocomplete': 'off', 'class': 'form-control form-control-sm text-center', 'onblur': 'guardarheredofamiliar();', 'onchange': 'guardarheredofamiliar();', 'data-toggle': 'tooltip', 'data-placement': 'left', 'title': ''})
            # form.field.widget.attrs['onblur'] = 'guardarheredofamiliar();'

    class Meta:
        exclude = ['propietario']
        model = AntecedenteFamiliar
        widgets = {
            'hermanos': NumberInput(attrs={'min': '0',  'data-original-title': 'No. Hermanos'}),
            'diabetes': TextInput(attrs={'data-original-title': 'Diabetes'}),
            'hip_arterial': TextInput(attrs={'data-original-title': 'Hipertensión Arterial'}),
            'cardiopatias': TextInput(attrs={'data-original-title': 'Cardiopatías'}),
            'hepatopatias': TextInput(attrs={'data-original-title': 'Hepatopatías'}),
            'urologicos': TextInput(attrs={'data-original-title': 'Urológicos'}),
            'neurologicos': TextInput(attrs={'data-original-title': 'Neurológicas'}),
            'respiratorios': TextInput(attrs={'data-original-title': 'Respiratorias'}),
            'cancer': TextInput(attrs={'data-original-title': 'Cancer'}),
            'alergias': TextInput(attrs={'data-original-title': 'Alérgicas'}),
            'metabolicas': TextInput(attrs={'data-original-title': 'Metabólicas'}),
            'sanguineas': TextInput(attrs={'data-original-title': 'Sanguíneas'}),
            'articulares': TextInput(attrs={'data-original-title': 'Articulares'}),
            'inmunologicas': TextInput(attrs={'data-original-title': 'Inmunológicas'}),
            'malformaciones': TextInput(attrs={'data-original-title': 'Malformaciones'}),
            'dermatologicas': TextInput(attrs={'data-original-title': 'Dermatológicas'}),
            'otros': TextInput(attrs={'data-original-title': 'Otros'}),
        }


class FormAntecedentePersonal(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update(
                {'autocomplete': 'off', 'class': 'form-control form-control-sm text-center', 'onblur': 'guardarNoPatologico();', 'onchange': 'guardarNoPatologico();', 'data-toggle': 'tooltip', 'data-placement': 'left', 'title': ''})
            # form.field.widget.attrs['onblur'] = 'guardarheredofamiliar();'
            # 'data-original-title':'Última Desparasitación'

    class Meta:
        model = AntecedentePersonal
        exclude = ['propietario']
        widgets = {
            'ultima_desparacita': TextInput(attrs={'data-original-title':'Última Desparasitación'}),
            'casa': TextInput(attrs={'data-original-title': 'Casa-Habitación'}),
            'lav_dientes': TextInput(attrs={'data-original-title': 'Lavado de dientes Diario'}),
            'tipo_pasta': TextInput(attrs={'data-original-title': 'Tipo de Pasta Dental'}),
            'amalgama_puente': TextInput(attrs={'data-original-title': 'Amalgamas o Puentes'}),
            'brakets': TextInput(attrs={'data-original-title': 'Brakets'}),
            'actividad_fisica': TextInput(attrs={'data-original-title': 'Actividad Física'}),
            'inmunizaciones': TextInput(attrs={'data-original-title': 'Inmunizaciones'}),
            'check_up': TextInput(attrs={'data-original-title': 'CheckUp Integral'}),
        }


class FormAntecedentePatologico(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update(
                {'class': 'form-control form-control-sm text-center', 'autocomplete': 'off', 'onblur': 'guardarAntecetentePatologico();', 'onchange': 'guardarAntecetentePatologico();', 'data-toggle': 'tooltip', 'data-placement': 'left', 'title': ''})
            # form.field.widget.attrs['onblur'] = 'guardarAntecetentePatologico();'

    class Meta:
        model = AntecedentePatologico
        exclude = ['propietario']
        widgets = {
            'enf_infancia': TextInput(attrs={'data-original-title': 'Enfermedades Propias de la Infancia'}),
            'diabetes': TextInput(attrs={'data-original-title': 'Diabetes'}),
            'hip_arterial': TextInput(attrs={'data-original-title': 'Hipertensión'}),
            'respiratorias': TextInput(attrs={'data-original-title': 'Respiratorias'}),
            'oftalmico': TextInput(attrs={'data-original-title': 'Oftálmico'}),
            'cardeovasculares': TextInput(attrs={'data-original-title': 'Cardiovasculares'}),
            'neurologicos': TextInput(attrs={'data-original-title': 'Neurológicos'}),
            'gastro_intestinal': TextInput(attrs={'data-original-title': 'Gastro-Intestinales'}),
            'hepaticas': TextInput(attrs={'data-original-title': 'Hepatopatías'}),
            'metabolicas': TextInput(attrs={'data-original-title': 'Metabólicas'}),
            'urologicos': TextInput(attrs={'data-original-title': 'Urológicos'}),
            'circulatorio': TextInput(attrs={'data-original-title': 'Circulatorio'}),
            'traumaticas': TextInput(attrs={'data-original-title': 'Traumáticas'}),
            'articulares': TextInput(attrs={'data-original-title': 'Articulares'}),
            'dermatologicas': TextInput(attrs={'data-original-title': 'Dermatológicas'}),
            'quirurgicas': TextInput(attrs={'data-original-title': 'Quirúrgicos'}),
            'transfusionales': TextInput(attrs={'data-original-title': 'Transfusionales'}),
            'alergias': TextInput(attrs={'data-original-title': 'Alergias'}),
            'vectores': TextInput(attrs={'data-original-title': 'Vectores'}),
            'autoimunes': TextInput(attrs={'data-original-title': 'Autoinmunes'}),
            'emocionales': TextInput(attrs={'data-original-title': 'Emocionales'}),
            'adicciones': TextInput(attrs={'data-original-title': 'Adicciones'}),
            'hosp_previas': TextInput(attrs={'data-original-title': 'Hospitalizaciones Previas'}),
            'pesticidas': TextInput(attrs={'data-original-title': 'Pesticidas'}),
            'dx_ca': TextInput(attrs={'data-original-title': 'Dx.CA.'}),
            'otros': TextInput(attrs={'data-original-title': 'Otros'}),
        }


class FormAntecedenteAlimenticio(ModelForm):
    class Meta:
        model = AntecedenteAlimenticio
        exclude = ['propietario']
        # fields = '__all__'


class FormExploracion(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update(
                {'class': 'form-control form-control-sm text-center', 'autocomplete': 'off', 'onblur': '', 'onchange': '', 'data-toggle': 'tooltip', 'data-placement': 'left', 'title': ''})
    class Meta:
        model = Exploracion
        exclude = ['propietario']
        # widgets = {
        #     'comidas':CheckboxSelectMultiple(attrs='')
        # }
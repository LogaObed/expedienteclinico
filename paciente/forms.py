from django.forms import ModelForm, DateInput, widgets
from paciente.models import *
 
class FormPaciente(ModelForm):
    class Meta:
        model = DatosGeneral
        fields = '__all__'
        widgets={
            'fecha_nacimiento': DateInput(attrs={'type':'date'})
        }

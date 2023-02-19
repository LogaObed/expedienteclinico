from django.shortcuts import render
from paciente.forms import FormPaciente
# Create your views here.
def paciente(request):
    form = FormPaciente
    return render(request,'base.html',{'form':form})
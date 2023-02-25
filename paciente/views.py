from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
import json
from paciente.forms import *
from django.core import serializers
from paciente.models import *
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
# Create your views here.


def inicio(request):
    return render(request, 'index.html')


def consultaPacientesajax(request):
    # 2. paciente 3. personal 4. contacto
    # people = serializers.serialize("json", Person.objects.all())
    data = list(Paciente.objects.filter(tipo_usuario=2).order_by('-id').values())  # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse({'datos':data}, safe=False) 

def consultaPacientes(request):
    # 2. paciente 3. personal 4. contacto
    form = FormNuevoPaciente()
    paciente = Paciente.objects.filter(tipo_usuario=2).order_by('-id')
    return render(request, 'paciente/consultapaciente.html', {'pacientes': paciente, 'form': form})


def nuevoPaciente(request):
    response_data = {}
    if request.method == 'GET':
        form = FormNuevoPaciente()
        paciente = Paciente.objects.filter(tipo_usuario=2)
        return render(request, 'paciente/consultapaciente.html', {'pacientes': paciente, 'form': form})
    else:
        form = FormNuevoPaciente(request.POST)
        if form.is_valid():
            form.save()
            # dato = Paciente.objects.all().order_by('-id')[:1]
            contulataPropietario = Paciente.objects.latest('id')
            idpropietario = contulataPropietario.id
            # DatosGeneral(propietario=idpropietario)
            # DatosGeneral(propietario=Paciente(id=idpropietario))
            propie = Paciente.objects.get(pk=idpropietario)
            # datos generales
            datosdeneral = DatosGeneral()
            datosdeneral.propietario = propie
            datosdeneral.save()
            # preferencia
            preferencia = Preferencia()
            preferencia.propietario = propie
            preferencia.save()
            # notapaciente
            notapaciente = NotaPaciente()
            notapaciente.propietario = propie
            notapaciente.save()
            # antecedentepersonal
            antecedentepersonal = AntecedentePersonal()
            antecedentepersonal.propietario = propie
            antecedentepersonal.save()
            # antecedentefamiliar
            antecedentefamiliar = AntecedenteFamiliar()
            antecedentefamiliar.propietario = propie
            antecedentefamiliar.save()
            # antecedentepatologico
            antecedentepatologico = AntecedentePatologico()
            antecedentepatologico.propietario = propie
            antecedentepatologico.save()
            # AntecedenteAlimenticio
            antecedentealimenticio = AntecedenteAlimenticio()
            antecedentealimenticio.propietario = propie
            antecedentealimenticio.save()
            # exploracion
            exploracion = Exploracion()
            exploracion.propietario = propie
            exploracion.save()
            # return redirect('consultapaciente')
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
        else:
            # return redirect('paciente')
            ctx = {}
            ctx.update(csrf(request))
            form_html = render_crispy_form(form, context=ctx)
            return {'success': False, 'form_html': form_html}


def editarPaciente(request, dato):
    userdata = get_object_or_404(Paciente, pk=dato)
    if request.method == 'GET':
        paciente = Paciente.objects.filter(id=dato)
        form = FormNuevoPaciente(instance=userdata)
        # datos generales
        cnsgeneral = DatosGeneral.objects.get(propietario=dato)
        dtid = cnsgeneral.id
        dtgeneral = get_object_or_404(DatosGeneral, pk=dtid)
        formgeneral = FormPacienteGeneral(instance=dtgeneral)
        # Preferencia
        cnpref = Preferencia.objects.get(propietario=dato)
        prefid = cnpref.id
        dtpref = get_object_or_404(Preferencia, pk=prefid)
        formpref = FormPreferencia(instance=dtpref)
        return render(request, 'paciente/editarpaciente.html', {'pacientes': paciente, 'formpref': formpref, 'formgeneral': formgeneral, 'form': form})
    else:
        form = FormNuevoPaciente(request.POST, instance=userdata)
        if form.is_valid():
            form.save()
            return redirect('consultapaciente')
        else:
            return redirect('paciente')


def consultaIndividualPaciente(request, dato):
    form = FormPacienteGeneral()
    datogeneral = get_object_or_404(DatosGeneral, pk=dato)
    return render(request, 'paciente/consutlaindividual.html', {'pacientea': datogeneral, 'form': form})


def formGeneral(request):
    # form = FormPaciente()
    return render(request, 'paciente/consultapaciente.html',)


def consultaUsuario(request):
    pacientes = Paciente.objects.all()
    data = list(pacientes)
    return JsonResponse({'dato': data})
    # tasks = Task.objects.filter(user=request.user, terminacion__isnull=False)
    # return JsonResponse(request,pacientes)


def consultaDatoGeneral(request, dato, propietario):
    propietario = propietario
    existe = DatosGeneral.objects.filter(propietario=dato).count()
    if existe == 0:
        return HttpResponse('no existe')
    else:
        return HttpResponse('si existe')
    # datogeneral = get_object_or_404(DatosGeneral, pk=dato)
    # form = FormPaciente(instance=datogeneral)
    # return render(request, 'consultapaciente.html', {'form': form})

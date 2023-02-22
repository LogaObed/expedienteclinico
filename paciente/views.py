from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from paciente.forms import *
from paciente.models import *
# Create your views here.


def inicio(request):
    return render(request, 'index.html')


def consultaPacientes(request):
    # 2. paciente 3. personal 4. contacto
    form = FormNuevoPaciente()
    paciente = Paciente.objects.filter(tipo_usuario=2)
    return render(request, 'paciente/consultapaciente.html', {'pacientes': paciente, 'form': form})


def nuevoPaciente(request):
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
            propie = Paciente.objects.get(pk = idpropietario)
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
            return redirect('consultapaciente')
        else:
            return redirect('paciente')


def editarPaciente(request, dato):
    userdata = get_object_or_404(Paciente, pk=dato)
    if request.method == 'GET':
        paciente = Paciente.objects.filter(id=dato)
        form = FormNuevoPaciente(instance=userdata)
        return render(request, 'paciente/editarpaciente.html', {'pacientes': paciente, 'form': form})
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
    form = FormPaciente()
    return render(request, 'paciente/consultapaciente.html', {'form': form})


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

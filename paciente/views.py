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


def editarPacienteAjax(request, dato):
    # response_data = {}
    if request.method == 'GET':
        userdata = get_object_or_404(Paciente, pk=dato)
        form = FormNuevoPaciente(instance=userdata)
        # form_html = form.as_table()
        return JsonResponse({'form_html': form})
        # return render(request, 'paciente/consultapaciente.html', {'pacientes': paciente, 'form': form})
    # else:
        # form = FormNuevoPaciente(request.POST)
        # if form.is_valid():
        #     form.save()
        #     # return redirect('consultapaciente')
        #     response_data['tipo'] = 'success'
        #     return JsonResponse(response_data)
        # else:
        #     # return redirect('paciente')
        #     ctx = {}
        #     ctx.update(csrf(request))
        #     form_html = render_crispy_form(form, context=ctx)
        #     return {'success': False, 'form_html': form_html}


def consultaPacientesajax(request):
    # 2. paciente 3. personal 4. contacto
    # people = serializers.serialize("json", Person.objects.all())
    # wrap in list(), because QuerySet is not JSON serializable
    data = list(Paciente.objects.filter(
        tipo_usuario=2).order_by('-id').values())
    return JsonResponse({'datos': data}, safe=False)


def consultaPacientes(request):
    # 2. paciente 3. personal 4. contacto
    form = FormNuevoPaciente()
    # paciente = DatosGeneral.objects.filter(tipo_usuario=2).order_by('-id')
    paciente = Paciente.objects.filter(tipo_usuario=2).order_by('-id')
    # return HttpResponse(paciente)
    return render(request, 'paciente/consultapaciente.html', {'pacientes': paciente, 'form': form})
    # return render(request, 'ejemplodivcartpaciente.html', {'pacientes': paciente, 'form': form})


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
    # return HttpResponse(userdata.preferencia.experiencia)
    if request.method == 'GET':
        paciente = Paciente.objects.get(id=dato)
        form = FormNuevoPaciente(instance=userdata)
        formSangre = FormTipoSangre(instance=userdata)
        formSexo = FormTipoSexo(instance=userdata)
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
        # NotaPaciente
        cnnota = NotaPaciente.objects.get(propietario=dato)
        notaid = cnnota.id
        dtnota = get_object_or_404(NotaPaciente, pk=notaid)
        formnota = FormNota(instance=dtnota)
        # AntecedentePersonal
        cnpersonal = AntecedentePersonal.objects.get(propietario=dato)
        personalid = cnpersonal.id
        dtpersonal = get_object_or_404(AntecedentePersonal, pk=personalid)
        formpersonal = FormAntecedentePersonal(instance=dtpersonal)
        # AntecedenteFamiliar
        cnfamiliar = AntecedenteFamiliar.objects.get(propietario=dato)
        familiarid = cnfamiliar.id
        dtfamiliar = get_object_or_404(AntecedenteFamiliar, pk=familiarid)
        formfamiliar = FormAntecedenteFamiliar(instance=dtfamiliar)
        # AntecedentePatologico
        cnpatologico = AntecedentePatologico.objects.get(propietario=dato)
        patologicoid = cnpatologico.id
        dtpatologico = get_object_or_404(
            AntecedentePatologico, pk=patologicoid)
        formpatologico = FormAntecedentePatologico(instance=dtpatologico)
        # AntecedenteAlimenticio
        cnalimenticios = AntecedenteAlimenticio.objects.get(propietario=dato)
        alimenticiosid = cnalimenticios.id
        dtalimenticios = get_object_or_404(
            AntecedenteAlimenticio, pk=alimenticiosid)
        formalimenticio = FormAntecedenteAlimenticio(instance=dtalimenticios)
        # Exploracion
        cnexporacion = Exploracion.objects.get(propietario=dato)
        exploracionid = cnexporacion.id
        dtexploracion = get_object_or_404(Exploracion, pk=exploracionid)
        formexploracion = FormExploracion(instance=dtexploracion)
        return render(request, 'paciente/editarpaciente.html', {'formSexo': formSexo, 'formSangre': formSangre, 'paciente': paciente, 'formexploracion': formexploracion, 'formpatologico': formpatologico, 'formalimenticio': formalimenticio, 'formfamiliar': formfamiliar, 'formpersonal': formpersonal, 'formnota': formnota, 'formpref': formpref, 'formgeneral': formgeneral, 'form': form})
    else:
        form = FormNuevoPaciente(request.POST, instance=userdata)
        if form.is_valid():
            form.save()
            return redirect('consultapaciente')
        else:
            return redirect('paciente')


def editarPreferencia(request, prefe):
    if request.method == "POST":
        response_data = {}
        # actualizar preferencia
        cnpref = Preferencia.objects.get(propietario=prefe)
        prefid = cnpref.id
        busca_prefe = get_object_or_404(Preferencia, pk=prefid)
        form = FormPreferencia(request.POST, instance=busca_prefe)
        if form.is_valid():
            form.save()
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
    else:
        response_data['tipo'] = 'get'
        return JsonResponse(response_data)


def editarDatoGeneral(request, datogeneral):
    if request.method == "POST":
        response_data = {}
        #
        cnsgeneral = DatosGeneral.objects.get(propietario=datogeneral)
        dtid = cnsgeneral.id
        busca_general = get_object_or_404(DatosGeneral, pk=dtid)
        form = FormPacienteGeneral(request.POST, instance=busca_general)
        if form.is_valid():
            form.save()
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
    else:
        response_data['tipo'] = 'get'
        return JsonResponse(response_data)


def editarHeredoFamiliar(request, heredofamiliar):
    if request.method == "POST":
        response_data = {}
        #
        conheredofamiliar = AntecedenteFamiliar.objects.get(
            propietario=heredofamiliar)
        dtid = conheredofamiliar.id
        busca = get_object_or_404(AntecedenteFamiliar, pk=dtid)
        form = FormAntecedenteFamiliar(request.POST, instance=busca)
        if form.is_valid():
            form.save()
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
    else:
        response_data['tipo'] = 'get'
        return JsonResponse(response_data)


def editarPatologicos(request, patologico):
    if request.method == "POST":
        response_data = {}
        consusulta = AntecedentePatologico.objects.get(
            propietario=patologico)
        dtid = consusulta.id
        busca = get_object_or_404(AntecedentePatologico, pk=dtid)
        form = FormAntecedentePatologico(request.POST, instance=busca)
        if form.is_valid():
            form.save()
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
    else:
        response_data['tipo'] = 'get'
        return JsonResponse(response_data)


def editarNoPatologicos(request, patologico):
    if request.method == "POST":
        response_data = {}
        consusulta = AntecedentePersonal.objects.get(
            propietario=patologico)
        dtid = consusulta.id
        busca = get_object_or_404(AntecedentePersonal, pk=dtid)
        form = FormAntecedentePersonal(request.POST, instance=busca)
        if form.is_valid():
            form.save()
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
    else:
        response_data['tipo'] = 'get'
        return JsonResponse(response_data)


def editaHalimenticio(request, habito):
    if request.method == "POST":
        response_data = {}
        consusulta = AntecedenteAlimenticio.objects.get(
            propietario=habito)
        dtid = consusulta.id
        busca = get_object_or_404(AntecedenteAlimenticio, pk=dtid)
        form = FormAntecedenteAlimenticio(request.POST, instance=busca)
        if form.is_valid():
            form.save()
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
    else:
        response_data['tipo'] = 'get'
        return JsonResponse(response_data)


def editaExploracion(request, exploracion):
    if request.method == "POST":
        response_data = {}
        consusulta = Exploracion.objects.get(
            propietario=exploracion)
        dtid = consusulta.id
        busca = get_object_or_404(Exploracion, pk=dtid)
        form = FormExploracion(request.POST, instance=busca)
        if form.is_valid():
            form.save()
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
    else:
        response_data['tipo'] = 'get'
        return JsonResponse(response_data)


def edtirarSexo(request, sexo):
    if request.method == "POST":
        response_data = {}
        busca = get_object_or_404(Paciente, pk=sexo)
        form = FormTipoSexo(request.POST, instance=busca)
        if form.is_valid():
            form.save()
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
    else:
        response_data['tipo'] = 'get'
        return JsonResponse(response_data)

def edtirarNotas(request, notas):
    if request.method == "POST":
        response_data = {}
        consusulta = NotaPaciente.objects.get(propietario=notas)
        dtid = consusulta.id
        busca = get_object_or_404(NotaPaciente, pk=dtid)
        form = FormNota(request.POST, instance=busca)
        if form.is_valid():
            form.save()
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
    else:
        response_data['tipo'] = 'get'
        return JsonResponse(response_data)


def edtirarSangre(request, sangre):
    if request.method == "POST":
        response_data = {}
        busca = get_object_or_404(Paciente, pk=sangre)
        form = FormTipoSangre(request.POST, instance=busca)
        if form.is_valid():
            form.save()
            response_data['tipo'] = 'success'
            return JsonResponse(response_data)
    else:
        response_data['tipo'] = 'get'
        return JsonResponse(response_data)


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

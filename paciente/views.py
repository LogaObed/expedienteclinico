from django.shortcuts import render

# Create your views here.
def paciente(request):
    return render(request,'base.html')
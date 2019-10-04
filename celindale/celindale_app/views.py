from django.shortcuts import render


# Create your views here.

def pasteleria(request):
    return render(request, 'pasteleria.html')


def home(request):
    return render(request, 'home.html')


def contacto(request):
    return render(request, 'contacto.html')


def banqueteria(request):
    return render(request, 'banqueteria.html')


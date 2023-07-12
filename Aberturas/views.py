from django.shortcuts import render, HttpResponse


def home(request):
  return render(request,"Aberturas/index.html")

def aberturas_aluminio(request):
  return render(request,"Aberturas/Aberturas_aluminio.html")

def aberturas_pvc(request):
  return render(request,"Aberturas/Aberturas_pvc.html")

def contacto(request):
  return render(request,"Aberturas/contactos.html")

# Create your views here.

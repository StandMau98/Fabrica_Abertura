from django.shortcuts import render, HttpResponse
from .models import Trabajo_PVC, Trabajo_Aluminio


def home(request):
  return render(request,"Aberturas/index.html")

def aberturas_aluminio(request):
  Aluminio = Trabajo_Aluminio.objects.all()
  return render(request,"Aberturas/Aberturas_aluminio.html",{'Aluminio':Aluminio})
  

def aberturas_pvc(request):
  PVC = Trabajo_PVC.objects.all()
  return render(request,"Aberturas/Aberturas_pvc.html",{"PVC":PVC})
  

def contacto(request):
  return render(request,"Aberturas/contactos.html")

# Create your views here.

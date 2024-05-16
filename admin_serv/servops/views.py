from django.shortcuts import render, redirect
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import Server, ServerType, User, Service, Application, ResourceUsage
from .forms import ServerForm, ServerTypeForm, UserForm, ServiceForm, ApplicationForm, ResourceUsageForm

## Créations des vues pour les index SR du site
def index(request):
    return render(request, 'servops/home.html')

def dashboard(request):
    return render(request, 'servops/dashboard.html')

def applications(request):
    return render(request, 'servops/CURD/CRUD_applications/home.html')

def servers(request):
    return render(request,'servops/CRUD/CRUD_serveurs/home.html')

def services(request):
    return render(request, 'servops/CURD/CRUD_services/home.html')
    
def server_types(request):
    return render(request, 'servops/CRUD/CRUD_type_serveurs/home.html')
    
def users(request):
    return render(request, 'servops/CRUD/CRUD_utilisateurs/home.html')


## CREATE_CRUD

def CreateServerVIew(request):
    if request.method == "POST":
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servops:index')
        else:
            form = ServerForm()
        return render(request, 'servops/CRUD/CRUD_serveurs/')



## Generation du rapport en PDF
def pdf(request):
    """
    Création d'un rapport pour les services réseaux
    """
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")


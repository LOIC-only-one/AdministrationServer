from django.shortcuts import render, redirect
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import Server, ServerType, User, Service, Application, ResourceUsage
from .forms import ServerForm, ServerTypeForm, UserForm, ServiceForm, ApplicationForm, ResourceUsageForm, GetIDForm

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
    users = User.objects.all()
    return render(request, 'servops/CRUD/CRUD_utilisateurs/home.html', {'users': users})


## CREATE_CRUD

def CreateServerView(request):
    if request.method == "POST":
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servops:index')
        else:
            form = ServerForm()
        return render(request, 'servops/CRUD/CRUD_serveurs/create_serveur.html')


def CreateUsersView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('affiche_users', id=user.id)
    else:
        form = UserForm()
    return render(request, 'servops/CRUD/CRUD_utilisateurs/create_user.html', {'form': form})

def DeleteUsersView(request):
    form = GetIDForm(request.POST or None)
    if form.is_valid():
        id = form.cleaned_data.get('id')
        obj = User.objects.get(id=id)
        obj.delete()
        return redirect('users_crud')
    return render(request, 'servops/CRUD/CRUD_utilisateurs/delete.html', {'form': form})


def ReadUsersView(request):
    form = GetIDForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        id = form.cleaned_data.get('id')
        return redirect('affiche_users', id=id)
    return render(request, 'servops/CRUD/CRUD_utilisateurs/read_user.html', {'form': form})


def AfficheUsersView(request, id):
    user = User.objects.get(id=id)
    return render(request, 'servops/CRUD/CRUD_utilisateurs/affiche.html', {'user': user})

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


from django.shortcuts import render, redirect, get_object_or_404
from io import BytesIO
from datetime import datetime
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .models import Server, ServerType, ServUser, Service, Application
from .forms import ServerForm, ServerTypeForm, UserForm, ServiceForm, ApplicationForm, GetIDForm, UploadForm
import csv

# Vues génériques pour les opérations CRUD
def list_view(request, model, template_name, context_name):
    """
    Permet de lister les éléments d'un modèle
    """
    items = model.objects.all()
    return render(request, template_name, {context_name: items})

def detail_view(request, model, template_name, context_name, id):
    """
    Permet d'afficher les détails d'un élément d'un modèle
    """
    item = get_object_or_404(model, id=id)
    return render(request, template_name, {context_name: item})

def create_view(request, form_class, template_name, success_url):
    """
    Permet de créer un élément d'un modèle
    """
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

def delete_view(request, model, success_url, id):
    """
    Permet de supprimer un élément d'un modèle
    """
    item = get_object_or_404(model, id=id)
    if request.method == "POST":
        item.delete()
        return redirect(success_url)
    return render(request, 'servops/CRUD/delete_template.html', {'item': item})

def update_view(request, model, form_class, template_name, success_url, id):
    """
    Permet de mettre à jour un élément d'un modèle
    """
    item = get_object_or_404(model, id=id)
    if request.method == "POST":
        form = form_class(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=item)
    return render(request, template_name, {'form': form})


# Fonctions spécifiques
def index(request):
    return render(request, 'servops/home.html')

def dashboard(request):
    servers = Server.objects.all()
    return render(request, 'servops/dashboard.html', {'servers': servers})

def applications(request):
    return render(request, 'servops/CURD/CRUD_applications/home.html')

def servers(request):
    servers = Server.objects.all()
    return render(request, 'servops/CRUD/CRUD_serveurs/home.html', {'servers': servers})

def services(request):
    services = Service.objects.all()
    servers = Server.objects.all()
    return render(request, 'servops/CRUD/CRUD_services/home.html', {'services': services, 'servers': servers})

def server_types(request):
    server_types = ServerType.objects.all()
    return render(request, 'servops/CRUD/CRUD_type_serveurs/home.html', {'server_types': server_types})

def users(request):
    users = ServUser.objects.all()
    return render(request, 'servops/CRUD/CRUD_utilisateurs/home.html', {'users': users})


# CRUD Server
def CreateServerView(request):
    return create_view(request, ServerForm, 'servops/CRUD/CRUD_serveurs/create_serveur.html', 'servers_crud')

def ReadServerView(request, id):
    return detail_view(request, Server, 'servops/CRUD/CRUD_serveurs/read_server.html', 'server', id)

def UpdateServerView(request, id):
    return update_view(request, Server, ServerForm, 'servops/CRUD/CRUD_serveurs/update_serveur.html', 'servers_crud', id)

def DeleteServerView(request, id):
    return delete_view(request, Server, 'servers_crud', id)

# CRUD Utilisateurs
def CreateUsersView(request):
    return create_view(request, UserForm, 'servops/CRUD/CRUD_utilisateurs/create_user.html', 'users_crud')

def ReadUsersView(request):
    return render(request, 'servops/CRUD/CRUD_utilisateurs/read_user.html', {'form': GetIDForm()})

def AfficheUsersView(request, id):
    return detail_view(request, ServUser, 'servops/CRUD/CRUD_utilisateurs/affiche.html', 'user', id)

def UpdateUsersView(request, id):
    return update_view(request, ServUser, UserForm, 'servops/CRUD/CRUD_utilisateurs/update_user.html', 'users_crud', id)

def UpdateUsersViewModificate(request, id):
    return update_view(request, ServUser, UserForm, 'servops/CRUD/CRUD_utilisateurs/update_user.html', 'users_crud', id)

def DeleteUsersView(request):
    form = GetIDForm(request.POST)
    if form.is_valid():
        id = form.cleaned_data.get('id')
        return delete_view(request, ServUser, 'users_crud', id)
    return render(request, 'servops/CRUD/CRUD_utilisateurs/delete.html', {'form': form})

# CRUD Applications
def applications_home(request):
    return list_view(request, Application, 'servops/CRUD/CRUD_applications/home.html', 'applications')

def create_application(request):
    return create_view(request, ApplicationForm, 'servops/CRUD/CRUD_applications/create_app.html', 'applications_home')

def update_application(request, application_id):
    return update_view(request, Application, ApplicationForm, 'servops/CRUD/CRUD_applications/update_app.html', 'applications_home', application_id)

def delete_application(request, application_id):
    return delete_view(request, Application, 'applications_home', application_id)

# CRUD Type Serveur
def CreateServerTypeView(request):
    return create_view(request, ServerTypeForm, 'servops/CRUD/CRUD_type_serveurs/create_type.html', 'server_types_crud')

def DeleteServerTypeView(request):
    form = GetIDForm(request.POST)
    if form.is_valid():
        id = form.cleaned_data.get('id')
        return delete_view(request, ServerType, 'server_types_crud', id)
    return render(request, 'servops/CRUD/CRUD_type_serveurs/delete.html', {'form': form})

def ReadServerTypeView(request):
    return render(request, 'servops/CRUD/CRUD_type_serveurs/read_type.html', {'form': GetIDForm()})

def AfficheServerTypeView(request, id):
    return detail_view(request, ServerType, 'servops/CRUD/CRUD_type_serveurs/affiche_type.html', 'server_type', id)

def UpdateServerTypeView(request, id):
    return update_view(request, ServerType, ServerTypeForm, 'servops/CRUD/CRUD_type_serveurs/update_type.html', 'server_types_crud', id)

def UpdateServerTypeViewModificate(request, id):
    return update_view(request, ServerType, ServerTypeForm, 'servops/CRUD/CRUD_type_serveurs/update_type.html', 'server_types_crud', id)

# CRUD Services
def CreateServiceView(request):
    return create_view(request, ServiceForm, 'servops/CRUD/CRUD_services/create_service.html', 'services_crud')

def ReadServiceView(request):
    return render(request, 'servops/CRUD/CRUD_services/read_service.html', {'form': GetIDForm()})

def DeleteServiceView(request):
    form = GetIDForm(request.POST)
    if form.is_valid():
        id = form.cleaned_data.get('id')
        return delete_view(request, Service, 'services_crud', id)
    return render(request, 'servops/CRUD/CRUD_services/delete_service.html', {'form': form})

def AfficheServiceView(request, id):
    return detail_view(request, Service, 'servops/CRUD/CRUD_services/affiche_service.html', 'service', id)

# Génération du rapport en PDF
def pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    services = Service.objects.all()
    y = 750
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, y, "Liste des Services")
    y -= 30
    for service in services:
        p.setFont("Helvetica", 12)
        p.drawString(100, y, f"Nom du Service: {service.name}")
        p.drawString(100, y-20, f"Date de Lancement: {service.launch_date}")
        p.drawString(100, y-40, f"Mémoire Disque Utilisée: {service.memory_used} Go")
        p.drawString(100, y-60, f"Mémoire Requise: {service.required_memory} Mo")
        y -= 80
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="liste_services.pdf")

# Importation des données via un fichier CSV
def import_data_home(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['service_csv']
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file, delimiter=',')
            for row in reader:
                try:
                    server = Server.objects.get(name=row[4])  # Assuming row[4] contains server name
                    launch_date = datetime.strptime(row[1], '%Y-%m-%d').date()  # Adjust date format as needed
                    Service.objects.get_or_create(
                        name=row[0],
                        launch_date=launch_date,
                        memory_used=int(row[2]),
                        required_memory=int(row[3]),
                        launch_server=server
                    )
                except Exception as e:
                    # Handle exceptions like missing server, incorrect date format, etc.
                    print(f"Error processing row: {row}, Error: {e}")
            return redirect('services_crud')
    else:
        form = UploadForm()
    return render(request, 'servops/FUNCTIONS/import.html', {'form': form})
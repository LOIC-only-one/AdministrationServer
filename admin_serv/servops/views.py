from django.shortcuts import render, redirect, get_object_or_404
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .models import Server, ServerType, ServUser, Service, Application, ResourceUsage
from .forms import ServerForm, ServerTypeForm, UserForm, ServiceForm, ApplicationForm, ResourceUsageForm, GetIDForm, ImportCSVForm

## Créations des vues pour les index SR du site
def index(request):
    return render(request, 'servops/home.html')

def dashboard(request):
    servers = Server.objects.all()
    return render(request, 'servops/dashboard.html', {'servers': servers})

def applications(request):
    services = Service.objects.all()
    return render(request, 'servops/CURD/CRUD_applications/home.html')

def servers(request):
    return render(request,'servops/CRUD/CRUD_serveurs/home.html')

def services(request):
    services = Service.objects.all()
    servers = Server.objects.all()
    return render(request, 'servops/CRUD/CRUD_services/home.html', {'services': services, 'servers': servers})
    
def server_types(request):
    server_types = ServerType.objects.all()
    return render(request, 'servops/CRUD/CRUD_type_serveurs/home.html', {'server_types': server_types} )
    
def users(request):
    users = ServUser.objects.all()
    return render(request, 'servops/CRUD/CRUD_utilisateurs/home.html', {'users': users})



## CRUD Server
def CreateServerView(request):
    if request.method == "POST":
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servops:index')
        else:
            form = ServerForm()
        return render(request, 'servops/CRUD/CRUD_serveurs/create_serveur.html')


## Crud Utilisateurs
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
        obj = ServUser.objects.get(id=id)
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
    user = ServUser.objects.get(id=id)
    return render(request, 'servops/CRUD/CRUD_utilisateurs/affiche.html', {'user': user})


def UpdateUsersView(request):
    form = GetIDForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        id = form.cleaned_data.get('id')
        return redirect('update_users', id=id)
    return render(request, 'servops/CRUD/CRUD_utilisateurs/update_user.html', {'form': form})

def UpdateUsersViewModificate(request, id):
    user = ServUser.objects.get(id=id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users_crud')
    else:
        form = UserForm(instance=user)
    return render(request, 'servops/CRUD/CRUD_utilisateurs/update_user.html', {'form': form})


## CRUD_Applications
def applications_home(request):
    applications = Application.objects.all()
    return render(request, 'servops/CRUD/CRUD_applications/home.html', {'applications': applications})

def create_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('applications_home')
    else:
        form = ApplicationForm()
    return render(request, 'servops/CRUD/CRUD_applications/create_app.html', {'form': form})

def update_application(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            return redirect('applications_home')
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'servops/CRUD/CRUD_applications/update_app.html', {'form': form})

def delete_application(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == "POST":
        application.delete()
        return redirect('applications_home')
    return render(request, 'servops/CRUD/CRUD_applications/delete_app.html', {'application': application})

## CRUD Type Serveur
def CreateServerTypeView(request):
    if request.method == "POST":
        form = ServerTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('server_types_crud')
    else:
        form = ServerTypeForm()
    return render(request, 'servops/CRUD/CRUD_type_serveurs/create_type.html', {'form': form})

def DeleteServerTypeView(request):
    form = GetIDForm(request.POST or None)
    if form.is_valid():
        id = form.cleaned_data.get('id')
        obj = ServerType.objects.get(id=id)
        obj.delete()
        return redirect('server_types_crud')
    return render(request, 'servops/CRUD/CRUD_type_serveurs/delete.html', {'form': form})

def ReadServerTypeView(request):
    form = GetIDForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        id = form.cleaned_data.get('id')
        return redirect('affiche_server_type', id=id)
    return render(request, 'servops/CRUD/CRUD_type_serveurs/read_type.html', {'form': form})

def AfficheServerTypeView(request, id):
    server_type = ServerType.objects.get(id=id)
    return render(request, 'servops/CRUD/CRUD_type_serveurs/affiche_type.html', {'server_type': server_type})

def UpdateServerTypeView(request):
    form = GetIDForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        id = form.cleaned_data.get('id')
        return redirect('update_server_type', id=id)
    return render(request, 'servops/CRUD/CRUD_type_serveurs/update_type.html', {'form': form})

def UpdateServerTypeViewModificate(request, id):
    server_type = ServerType.objects.get(id=id)
    if request.method == "POST":
        form = ServerTypeForm(request.POST, instance=server_type)
        if form.is_valid():
            form.save()
            return redirect('server_types_crud')
    else:
        form = ServerTypeForm(instance=server_type)
    return render(request, 'servops/CRUD/CRUD_type_serveurs/update_type.html', {'form': form})

## CRUD Services
## Attention, il manque la vue pour l'update + Lien avec le serveur pour savoir si il a assez de ressources

def ReadServiceView(request):
    form = GetIDForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        id = form.cleaned_data.get('id')
        return redirect('affiche_service', id=id)
    return render(request, 'servops/CRUD/CRUD_services/read_service.html', {'form': form})

def DeleteServiceView(request):
    form = GetIDForm(request.POST or None)
    if form.is_valid():
        id = form.cleaned_data.get('id')
        obj = Service.objects.get(id=id)
        obj.delete()
        return redirect('services_crud')
    return render(request, 'servops/CRUD/CRUD_services/delete.html', {'form': form})

def AfficheServiceView(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'servops/CRUD/CRUD_services/affiche_service.html', {'service': service})

def CreateServiceView(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services_crud')
    else:
        form = ServiceForm()
    return render(request, 'servops/CRUD/CRUD_services/create_service.html', {'form': form})


## CRUD Serveur

def servers(request):
    servers = Server.objects.all()
    return render(request, 'servops/CRUD/CRUD_serveurs/home.html', {'servers': servers})

def CreateServerView(request):
    if request.method == "POST":
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servers_crud')
    else:
        form = ServerForm()
    return render(request, 'servops/CRUD/CRUD_serveurs/create_serveur.html', {'form': form})

def ReadServerView(request):
    form = GetIDForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        id = form.cleaned_data.get('id')
        return redirect('read_server', id=id)
    return render(request, 'servops/CRUD/CRUD_serveurs/read_server.html', {'form': form})

def AfficheServerView(request, id):
    server = get_object_or_404(Server, id=id)
    return render(request, 'servops/CRUD/CRUD_serveurs/read_server.html', {'server': server})

def UpdateServerView(request, id):
    server = get_object_or_404(Server, id=id)
    if request.method == "POST":
        form = ServerForm(request.POST, instance=server)
        if form.is_valid():
            form.save()
            return redirect('servers_crud')
    else:
        form = ServerForm(instance=server)
    return render(request, 'servops/CRUD/CRUD_serveurs/update_serveur.html', {'form': form})

def DeleteServerView(request, id):
    server = get_object_or_404(Server, id=id)
    if request.method == "POST":
        server.delete()
        return redirect('servers_crud')
    return render(request, 'servops/CRUD/CRUD_serveurs/delete_serveur.html', {'server': server})



## Generation du rapport en PDF
def pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    services = Service.objects.all()
    y = 750
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, y, "Liste des Services")
    y = y - 30
    for service in services:
        p.setFont("Helvetica", 12)
        p.drawString(100, y, f"Nom du Service: {service.name}")
        p.drawString(100, y-20, f"Date de Lancement: {service.launch_date}")
        p.drawString(100, y-40, f"Mémoire Disque Utilisée: {service.memory_used} Go")
        p.drawString(100, y-60, f"Mémoire Requise: {service.required_memory} Mo")
        y = y - 80
        ## Espace entre les services
        y = y - 20 
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="liste_services.pdf")

## Importation des données via un fichier CSV


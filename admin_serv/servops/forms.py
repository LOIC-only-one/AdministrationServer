from django import forms
from .models import Server, ServerType, ServUser, Service, Application, ResourceUsage

class ServerForm(forms.ModelForm):
    name = forms.CharField(label='Nom')
    server_type = forms.ModelChoiceField(queryset=ServerType.objects.all(), label='Type de serveur')
    num_processors = forms.IntegerField(label='Nombre de processeurs')
    memory_capacity = forms.IntegerField(label='Capacité mémoire')
    storage_capacity = forms.IntegerField(label='Capacité de stockage')

    class Meta:
        model = Server
        fields = ['name', 'server_type', 'num_processors', 'memory_capacity', 'storage_capacity']

class ServerTypeForm(forms.ModelForm):
    type = forms.CharField(label='Type')
    description = forms.CharField(label='Description')

    class Meta:
        model = ServerType
        fields = ['type', 'description']

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='Nom')
    last_name = forms.CharField(label='Prénom')
    email = forms.EmailField(label='Email')

    class Meta:
        model = ServUser
        fields = ['first_name', 'last_name', 'email']
        
class ServiceForm(forms.ModelForm):
    name = forms.CharField(label='Nom du service')
    launch_date = forms.DateField(label='Date de lancement')
    memory_used = forms.IntegerField(label='Espace mémoire disque utilisé (en Go)')
    required_memory = forms.IntegerField(label='Mémoire vive nécessaire (en Go)')
    launch_server = forms.ModelChoiceField(queryset=Server.objects.all(), label='Serveur de lancement')
        
    class Meta:
        model = Service
        fields = ['name', 'launch_date', 'memory_used', 'required_memory', 'launch_server']
        
class ApplicationForm(forms.ModelForm):
    name = forms.CharField(label='Nom de l\'application')
    logo = forms.ImageField(label='Logo')
    user = forms.ModelChoiceField(queryset=ServUser.objects.all(), label='Utilisateur')
    launch_server = forms.ModelChoiceField(queryset=Server.objects.all(), label='Serveur de lancement')
    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), label='Services')

    class Meta:
        model = Application
        fields = ['name', 'logo', 'user', 'launch_server', 'services']

class ResourceUsageForm(forms.ModelForm):
    application = forms.ModelChoiceField(queryset=Application.objects.all(), label='Application')
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label='Service')

    class Meta:
        model = ResourceUsage
        fields = ['application', 'service']
        
class GetIDForm(forms.Form):
    id = forms.IntegerField()
    
class ImportCSVForm(forms.Form):
    csv_file = forms.FileField(label="Importer un fichier CSV")
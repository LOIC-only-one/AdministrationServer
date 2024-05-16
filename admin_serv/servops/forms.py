from django import forms
from .models import Server, ServerType, User, Service, Application, ResourceUsage

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
    name = forms.CharField(label='Nom')
    surname = forms.CharField(label='Prénom')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['name', 'surname', 'email']

class ServiceForm(forms.ModelForm):
    name = forms.CharField(label='Nom du service')
    launch_date = forms.DateField(label='Date de lancement')
    memory_used = forms.IntegerField(label='Espace mémoire utilisé')
    required_memory = forms.IntegerField(label='Mémoire vive nécessaire')
    launch_server = forms.ModelChoiceField(queryset=Server.objects.all(), label='Serveur de lancement')

    class Meta:
        model = Service
        fields = ['name', 'launch_date', 'memory_used', 'required_memory', 'launch_server']

class ApplicationForm(forms.ModelForm):
    name = forms.CharField(label='Nom de l\'application')
    logo = forms.ImageField(label='Logo')
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='Utilisateur')

    class Meta:
        model = Application
        fields = ['name', 'logo', 'user']

class ResourceUsageForm(forms.ModelForm):
    application = forms.ModelChoiceField(queryset=Application.objects.all(), label='Application')
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label='Service')

    class Meta:
        model = ResourceUsage
        fields = ['application', 'service']
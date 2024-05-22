from django.db import models

class ServerType(models.Model):
    type = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.type

class Server(models.Model):
    name = models.CharField(max_length=200)
    server_type = models.ForeignKey(ServerType, on_delete=models.CASCADE, related_name='servers')
    num_processors = models.IntegerField()
    memory_capacity = models.IntegerField()
    storage_capacity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    launch_date = models.DateField()
    memory_used = models.IntegerField()
    required_memory = models.IntegerField()
    launch_server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='services')

class ServUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Application(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/')
    user = models.ForeignKey(ServUser, on_delete=models.CASCADE, related_name='applications')
    services = models.ManyToManyField(Service, related_name='applications')
    
class ResourceUsage(models.Model):
    ## Pas de update + Affichage sur la page des applications
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='resource_usages')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='resource_usages')
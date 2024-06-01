from django.urls import path
from . import views

urlpatterns = [
    
    ## MAIN ROOT
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    ## CRUD ROOT 
    path('applications/', views.applications, name='applications_crud'),
    path('servers/', views.servers, name='servers_crud'),
    path('service/', views.services, name='services_crud'),
    path('server_types/', views.server_types, name='server_types_crud'),
    path('users/', views.users, name='users_crud'),

    ## FONCTIONS
    path('file/', views.pdf, name='pdf'),
    path('import-csv/', views.import_csv_view, name='import_csv'),

    ## CRUD SERVEURS
    path('servers/create/', views.CreateServerView, name='create_server'),
    path('servers/update/<int:id>/', views.UpdateServerView, name='update_server'),
    path('servers/delete/<int:id>/', views.DeleteServerView, name='delete_server'),
    path('servers/', views.servers, name='servers_list'),
    
    ## CRUD SERVICES
    path('service/create/', views.CreateServiceView, name='create_service'),
    path('service/update/<int:id>/', views.UpdateServiceView, name='update_service'),
    path('service/delete/<int:id>/', views.DeleteServiceView, name='delete_service'),
    path('service/<int:id>/', views.AfficheServiceView, name="affiche_service"),
    
    
    ## CRUD USERS
    path('users/create/', views.CreateUsersView, name='create_users'),
    path('users/<int:id>/', views.AfficheUsersView, name="affiche_users"),
    path('users/update/<int:id>/', views.UpdateUsersViewModificate, name='update_users'),
    path('users/delete/<int:id>/', views.DeleteUsersView, name='delete_users'),

    ## CRUD SERVER TYPES
    path('server_types/create/', views.CreateServerTypeView, name='create_server_type'),
    path('server_types/<int:id>/', views.AfficheServerTypeView, name="affiche_server_type"),
    path('server_types/update/<int:id>/', views.UpdateServerTypeViewModificate, name='update_server_type'),
    path('server_types/delete/<int:id>/', views.DeleteServerTypeView, name='delete_server_type'),

    ## CRUD APPLICATION
    path('applications/home/', views.applications_home, name='applications_home'),
    path('applications/create/', views.create_application, name='create_application'),
    path('applications/update/<int:application_id>/', views.update_application, name='update_application'),
    path('applications/delete/<int:application_id>/', views.delete_application, name='delete_application'),

    ## CRUD RESOURCE USAGE
    #path('resource_usage/home/', views.resource_usage_home, name='resource_usage_home'),
    #path('resource_usage/create/', views.create_resource_usage, name='create_resource_usage'),
    #path('resource_usage/update/<int:resource_usage_id>/', views.update_resource_usage, name='update_resource_usage'),
    #path('resource_usage/delete/<int:resource_usage_id>/', views.delete_resource_usage, name='delete_resource_usage'),
    
]

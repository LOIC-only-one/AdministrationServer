from django.urls import path
from . import views

urlpatterns = [
    
    ## MAIN ROOT
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    ## CRUD ROOT 
    path('applications/', views.applications, name='applications_crud'),
    path('servers/', views.servers, name='servers_crud'),
    path('services/', views.services, name='services_crud'),
    path('server_types/', views.server_types, name='server_types_crud'),
    path('users/', views.users, name='users_crud'),

    ## FONCTIONS
    path('file/', views.pdf, name='pdf'),

    ## CRUD SERVEURS
    path('servers/create/', views.CreateServerView, name='create_server'),
    #path('servers/read/>/', views.ReadServerView, name='read_server'),
    #path('servers/update/<int:pk>/', views.UpdateServerView, name='update_server'),
    #path('servers/delete/', views.DeleteServerView, name='delete_server'),
    #path('servers/<int:id>/', views.AfficheServerView, name="affiche_server"),
    
    ## CRUD USERS
    path('users/create/', views.CreateUsersView, name='create_users'),
    path('users/delete/', views.DeleteUsersView, name='delete_users'),
    path('users/<int:id>/', views.AfficheUsersView, name="affiche_users"),
    path('users/read/', views.ReadUsersView, name='read_users'),
    #path('users/update/<int:id>/', views.UpdateUsersView, name='update_users')

    ## CRUD SERVER TYPES
    #path('server_types/create/', views.CreateServerTypeView, name='create_server_type'),
    #path('server_types/delete/', views.DeleteServerTypeView, name='delete_server_type'),
    #path('server_types/<int:id>/', views.AfficheServerTypeView, name="affiche_server_type"),
    #path('server_types/read/', views.ReadServerTypeView, name='read_server_type'),
    #path('server_types/update/<int:id>/', views.UpdateServerTypeView, name='update_server_type')

    ## CRUD APPLICATION
    path('applications/home/', views.applications_home, name='applications_home'),
    path('applications/create/', views.create_application, name='create_application'),
    path('applications/update/<int:application_id>/', views.update_application, name='update_application'),
    path('applications/delete/<int:application_id>/', views.delete_application, name='delete_application'),
]

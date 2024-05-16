from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('file/', views.pdf, name='pdf'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('applications/', views.applications, name='applications_crud'),
    path('servers/', views.servers, name='servers_crud'),
    path('services/', views.services, name='services_crud'),
    path('server_types/', views.server_types, name='server_types_crud'),
    path('users/', views.users, name='users_crud'),
]
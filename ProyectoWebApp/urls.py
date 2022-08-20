from django.urls import path
from ProyectoWebApp import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('Tienda/', views.tienda, name="Tienda"),
    path('Blog/', views.blog, name="Blog"),
    path('Contacto/', views.contacto, name="Contacto"),
]
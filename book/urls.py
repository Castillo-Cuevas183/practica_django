from django.urls import path
from . import views
from .views import list_books
from django.views.generic import TemplateView


urlpatterns = [
    # Rutas para las aplicaciones de Django
    path('', views.index, name='index'),  # Ruta principal que hace referencia a la vista index
    path('book/', views.index, name='book_index'),  # Redirige a index cuando accedes a /book
    path('palindrome/<str:word>/', views.check_palindrome, name='check_palindrome'),  # Nueva ruta
    path('libros/', views.libros, name='libros'),  # Vista para la sección Libros
    path('acerca_de/', views.acerca_de, name='acerca_de'),  # Vista para Acerca de
    path('contacto/', views.contacto, name='contacto'),  # Vista para Contacto
    path('listbook/', list_books, name='list_books'),  # Vista para listar libros
    path('inputbook/', views.input_book, name='inputbook'),
    path('registro/', views.registro, name='registro'),  # Ruta para el registro de usuarios
    path('accounts/profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),  # Vista para la ruta de perfil
]



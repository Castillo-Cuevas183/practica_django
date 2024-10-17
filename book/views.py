from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import BookForm  # Correcto, importa desde 'forms.py'
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from book.models import Libro

def check_palindrome(request, word):
    # Limpiar la palabra (quitar espacios y convertir a minúsculas)
    cleaned_word = ''.join(word.split()).lower()
    # Verificar si es un palíndromo
    is_palindrome = cleaned_word == cleaned_word[::-1]
    
    if is_palindrome:
        result = f"La palabra o frase '{word}' es un palíndromo."
    else:
        result = f"La palabra o frase '{word}' no es un palíndromo."
    
    return HttpResponse(result)

#Vista ingreso de Libro
def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros')  # Redirige después de agregar el libro
    else:
        form = BookForm()
    return render(request, 'book/input_book.html', {'form': form})


# vista registro usuario
def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registro.html', {'form': form})



def index(request):
    return render(request, 'index.html')

def libros(request):
    return render(request, 'libros.html')  # Asegúrate de crear 'libros.html'

def acerca_de(request):
    return render(request, 'acerca_de.html')  # Asegúrate de crear 'acerca_de.html'

def contacto(request):
    return render(request, 'contacto.html')  # Asegúrate de crear 'contacto.html'

# def list_books(request):
#     libros_mayor_1500 = [
#         {'titulo': 'Django 3 Web Development Cookbook Fourth Edition', 'autor': 'Aidas Bendoraitis', 'valoracion': 3250},
#         {'titulo': 'Two Scoops of Django 3.x', 'autor': 'Daniel Feldroy', 'valoracion': 1570},
#         {'titulo': 'Django for Professionals', 'autor': 'William S. Vincent', 'valoracion': 2100},
#         {'titulo': 'Django for APIs', 'autor': 'William S. Vincent', 'valoracion': 2540},
#     ]

#     todos_los_libros = [
#         {'titulo': 'Django 3 Web Development Cookbook Fourth Edition', 'autor': 'Aidas Bendoraitis'},
#         {'titulo': 'Two Scoops of Django 3.x', 'autor': 'Daniel Feldroy'},
#         {'titulo': 'El libro de Django', 'autor': 'Adrian Holovaty'},
#         {'titulo': 'Python Web Development with Django', 'autor': 'Jeff Forcier'},
#         {'titulo': 'Django for Professionals', 'autor': 'William S. Vincent'},
#         {'titulo': 'Django for APIs', 'autor': 'William S. Vincent'},
#     ]

#     return render(request, 'list_books.html', {
#         'libros_mayor_1500': libros_mayor_1500,
#         'todos_los_libros': todos_los_libros
#     })
    

# def list_books(request):
#     libros_mayor_1500 = Libro.objects.filter(valoracion__gt=1500)  # Filtra libros con valoración > 1500
#     todos_los_libros = Libro.objects.all()  # Obtiene todos los libros

#     return render(request, 'list_books.html', {
#         'libros_mayor_1500': libros_mayor_1500,
#         'todos_los_libros': todos_los_libros
#     })
    

def list_books(request):
    libros = Libro.objects.all()  # Obtén todos los libros de la base de datos
    return render(request, 'list_books.html', {'libros': libros})
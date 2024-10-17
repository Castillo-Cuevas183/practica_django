from django import forms
from .models import Libro  # Si estás utilizando un modelo llamado 'Libro'
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulario para crear un libro
class BookForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'valoracion']
        


# Formulario para el registro de usuarios
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

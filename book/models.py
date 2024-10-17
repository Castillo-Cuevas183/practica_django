from django.db import models
from django.utils import timezone

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    valoracion = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Cambia a default
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("development", "Permiso como Desarrollador"),
            ("scrum_master", "Permiso como Scrum Master"),
            ("product_owner", "Permiso como Product Owner"),
        ]
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.titulo

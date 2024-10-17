from django.contrib import admin
from .models import Libro

# class LibroAdmin(admin.ModelAdmin):
#     list_display = ('titulo', 'autor', 'valoracion', 'fecha_creacion', 'fecha_modificacion')
#     search_fields = ('titulo', 'autor')

# admin.site.register(Libro, LibroAdmin)



class LibroAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista
    list_display = ('titulo', 'valoracion', 'fecha_modificacion','rating')
    # Campos por los que se puede filtrar
    list_filter = ('valoracion', 'fecha_modificacion')
    # Campos que se mostrarán en la vista de detalle
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')  # Solo lectura
    # Opcional: si quieres que la fecha de creación y modificación se muestre en el formulario de edición
    fields = ('titulo', 'autor', 'valoracion', 'fecha_creacion', 'fecha_modificacion')
    
    def rating(self, obj):
        """Campo dinámico para mostrar el rating basado en la valoración."""
        if obj.valoracion < 1000:
            return "Baja"
        elif 1000 <= obj.valoracion <= 2500:
            return "Media"
        else:
            return "Alta"
    rating.short_description = 'Rating'
    
admin.site.register(Libro, LibroAdmin)
from django.db import models

# Definición del modelo Tarea
class Tarea(models.Model):
    # Campo de texto para el título de la tarea
    titulo = models.CharField(max_length=200)
    
    # Campo de texto largo para la descripción de la tarea
    descripcion = models.TextField()
    
    # Campo booleano para indicar si la tarea está completada o no
    completado = models.BooleanField(default=False)

    # Método para representar la tarea como una cadena de texto
    def __str__(self):
        return self.titulo

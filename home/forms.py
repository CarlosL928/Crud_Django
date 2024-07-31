from django import forms  # Importamos el módulo forms de Django
from .models import Tarea  # Importamos el modelo Tarea desde el archivo models.py

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea  # Especificamos el modelo Tarea al que está asociado el formulario
        fields = ['titulo', 'descripcion', 'completado']  # Definimos los campos del formulario
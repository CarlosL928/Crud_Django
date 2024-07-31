from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm

# Vista para mostrar la lista de tareas
def lista_tareas(request):
    # Obtener todas las tareas de la base de datos
    tareas = Tarea.objects.all()
    # Renderizar la plantilla 'lista_tareas.html' y pasar las tareas como contexto
    return render(request, 'home/lista_tareas.html', {'tareas': tareas})

# Vista para mostrar los detalles de una tarea específica
def detalle_tarea(request, pk):
    # Obtener la tarea correspondiente al ID proporcionado, o mostrar un error 404 si no existe
    tarea = get_object_or_404(Tarea, pk=pk)
    # Renderizar la plantilla 'detalle_tarea.html' y pasar la tarea como contexto
    return render(request, 'home/detalle_tarea.html', {'tarea': tarea})

# Vista para crear una nueva tarea
def nueva_tarea(request):
    if request.method == "POST":
        # Si se envió un formulario por el método POST, procesarlo
        form = TareaForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guardar la tarea en la base de datos
            tarea = form.save(commit=False)
            tarea.save()
            # Redirigir a la vista de detalles de la nueva tarea creada
            return redirect('detalle_tarea', pk=tarea.pk)
    else:
        # Si no se envió un formulario por el método POST, mostrar un formulario vacío
        form = TareaForm()
    # Renderizar la plantilla 'editar_tarea.html' y pasar el formulario como contexto
    return render(request, 'home/editar_tarea.html', {'form': form})

# Vista para editar una tarea existente
def editar_tarea(request, pk):
    # Obtener la tarea correspondiente al ID proporcionado, o mostrar un error 404 si no existe
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        # Si se envió un formulario por el método POST, procesarlo
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            # Si el formulario es válido, guardar los cambios en la tarea en la base de datos
            tarea = form.save(commit=False)
            tarea.save()
            # Redirigir a la vista de detalles de la tarea editada
            return redirect('detalle_tarea', pk=tarea.pk)
    else:
        # Si no se envió un formulario por el método POST, mostrar el formulario con los datos de la tarea existente
        form = TareaForm(instance=tarea)
    # Renderizar la plantilla 'editar_tarea.html' y pasar el formulario como contexto
    return render(request, 'home/editar_tarea.html', {'form': form})

# Vista para eliminar una tarea
def eliminar_tarea(request, pk):
    # Obtener la tarea correspondiente al ID proporcionado, o mostrar un error 404 si no existe
    tarea = get_object_or_404(Tarea, pk=pk)
    # Eliminar la tarea de la base de datos
    tarea.delete()
    # Redirigir a la vista de lista de tareas
    return redirect('lista_tareas')
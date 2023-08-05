from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

def addtask(request):
    task = request.POST['task'] #POST['task'] is the key(name) of input element which stores data.
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if task.is_completed == True:
        task.is_completed = False
        task.save()
    return redirect('home')

def edit(request,pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        updated_task = request.POST['task'] # the name in the input tag
        get_task.task = updated_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'edit_task.html', context)


def delete_task(request,pk):
    get_task = get_object_or_404(Task, pk=pk)    
    get_task.delete()
    return redirect('home')


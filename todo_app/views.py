from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

def addtask(request):
    task = request.POST['task'] #POST['task'] is the key(name) of input element which stores data.
    Task.objects.create(task=task)
    return redirect('home')




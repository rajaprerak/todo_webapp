from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)


def update_task(request, key):
    task = Task.objects.get(id=key)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "todo/update_task.html", context)


def delete(request, key):
    item = Task.objects.get(id=key)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, "todo/delete.html", context)

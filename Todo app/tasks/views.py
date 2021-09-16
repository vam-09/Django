from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    # print(tasks)
    form = TaskForm()

    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        "tasks" : tasks,
        "form" : form,
    }
    return render(request,"index.html",context)

def updateTask(request,pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        form.save()
        return redirect("/")
    context = {
        "form" : form,
    }

    return render(request,"update_task.html",context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
 
    if request.method=="POST":
        item.delete()
        return redirect('/')
    context = {
        "item" : item,
    }

    return render(request,"delete.html",context)

def trial(request):
    cities = [
    {'name': 'Mumbai', 'population': '7,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'Japan'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
    ]
    context = {"cities" : cities}
    return render(request,"trial.html",context)
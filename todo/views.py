from django.shortcuts import redirect, render
from .models import Tasks

def addtask(request):
    
    Tasks.objects.create(taskname=request.POST['task'])
    return redirect('home')

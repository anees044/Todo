from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Tasks

def addtask(request):
    
    Tasks.objects.create(taskname=request.POST['task'])
    return redirect('home')

def markasdone(request,pk):
    task=get_object_or_404(Tasks,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def markasundone(request,pk):
    task=get_object_or_404(Tasks,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def updatetask(request,pk):
    task=get_object_or_404(Tasks,pk=pk)
    if request.method=='POST':
        modifiedtask=request.POST['task']
        task.taskname=modifiedtask
        task.save()
        return redirect('home')
    else:
        context={
            'task':task
            }
        return render(request,'updatetask.html',context)
    
def deletetask(request,pk):
    task=get_object_or_404(Tasks,pk=pk)
    task.delete()
    return redirect('home')



from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Tasks



def home(request):
    tasks=Tasks.objects.filter(is_completed=False).order_by('-createdat')
    context={
        'tasks':tasks
        }
    return render(request,'home.html',context)
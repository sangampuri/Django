from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def tasks_list(request):
    return render(request,'tasks_list.html' )

def create_task(request):
    return render(request,'create_task.html' )

def store_task(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed') == 'on'

        if title and description:
            task = Task(title=title, description=description, is_completed=is_completed)
            task.save()
            return redirect('tasks_list')

    return render(request, 'create_task.html', {'error': 'Please fill in all fields.'})
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Task

# Create your views here.
def tasks_list(request):
    tasks = Task.objects.all()
    return render(request,'tasks_list.html' , {'tasks':tasks})

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

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title and description:
            task.title = title
            task.description = description
            task.is_completed = request.POST.get('is_completed') == 'on'
            task.save()
            return redirect('tasks_list')

        return render(request, 'edit_task.html', {
            'task': task,
            'error': 'Please fill in all fields.',
        })

    return render(request, 'edit_task.html', {'task': task})
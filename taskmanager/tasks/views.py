from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm


def main_page(request):
    all_tasks = Task.objects.all()
    context = {'tasks': all_tasks}
    return render(request, 'tasks_list.html', context=context)


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    context = {'task': task}
    return render(request, 'task_detail.html', context=context)


def create_task(request):
    # POST, GET, PUT
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-page')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', locals())


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('main-page')
    return render(request, 'delete_task.html')


def change_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('main-page')
    else:
        form = TaskForm(initial={
            'title': task.title, 
            'content': task.content, 
            'done': task.done
        })
    return render(request, 'task_change.html', locals())
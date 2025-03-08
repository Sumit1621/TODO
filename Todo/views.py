from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect
# from django.urls import reverse

# Create your views here.
def home(request):
    all_todos = Todo.objects.all()
    d = {'all_todos': all_todos}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        TO = Todo(title=title, desc=desc)
        TO.save()
    return render(request, 'home.html', d)

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('home')
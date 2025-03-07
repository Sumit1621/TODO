from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django .urls import reverse

# Create your views here.

def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    d = {'todo': todo}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        todo.title = title
        todo.desc = desc
        todo.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'update.html',d)

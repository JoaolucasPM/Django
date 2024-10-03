from django.shortcuts import render
from django.views.generic import ListView
from .models import Todos

def home(request):
    return render(request, "base.html")

class ProductListView(ListView):
    model = Todos
    template_name = 'todos/list.html'  # Aponta para o template
    context_object_name = 'listP'  # Define o nome do contexto no template

def form(request):
    return render(request, "todos/form.html")




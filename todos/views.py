from django.shortcuts import render
from .models import Todos
from django.views.generic import ListView

def home(request):
    return render(request, "base.html")

class ProductListView(ListView):
    model = Todos
    template_name = 'todos/list.html'  
    context_object_name = 'listP'  


def form(request):
    return render(request, "todos/form.html")




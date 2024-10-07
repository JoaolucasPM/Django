from django.shortcuts import render
from .models import Todos
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

def home(request):
    return render(request, "base.html")

class ProductListView(ListView):
    model = Todos
    template_name = 'todos/list.html'  
    context_object_name = 'listP'  

class ProductCreateView(CreateView):
    model = Todos
    template_name = 'todos/form.html'  
    fields = ["nome", "cidade"] #Campos que aparecerão
    success_url = reverse_lazy("list")




""" def form(request):
    return render(request, "todos/form.html")
    sucess_url = reverse_lazy("list") """




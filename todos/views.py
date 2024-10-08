from django.shortcuts import render
from .models import Todos
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

def home(request):
    return render(request, "base.html")

class ProductListView(ListView):
    model = Todos
    template_name = 'todos/list.html'  
    context_object_name = 'listP'  

class ProductCreateView(CreateView):
    model = Todos
    template_name = 'todos/form.html'  
    fields = ["nome", "cidade"] 
    success_url = reverse_lazy("list")

class ProductDeleteView(DeleteView):
    model = Todos
    success_url = reverse_lazy("list")

class ProductUpdateView(UpdateView):
    model = Todos
    fields = ["nome", "cidade"]
    template_name = 'todos/edit.html'  
    success_url = reverse_lazy("list")

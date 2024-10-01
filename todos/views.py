from django.shortcuts import render

def home(request):
    return render(request, "base.html")

def form(request):
    return render(request, "todos/form.html")



# Projeto django

Crie um ambiente virtual


```
python -m venv .venv
```

Ativar o ambiente

```
.\.venv\Scripts\activate
```

# Instalar o django com pip

</br> 

```
pip install django
```

## Criar o App
</br> 

```
django-admin startproject setup .
```
</br> 

## Criar o projeto

```
python manage.py startapp todos
```
 
# Add. o app dentro do setup
### Caminho das pastas
- todos > apps 
- todos > apps > TodosConfig (nome da função)

<br>

# Próximo passo (view)
Dentro da do projeto (todos)
##
- todos > criar pasta (templates) > criar uma mesma pasta com o nome do projeto (todos)
- P(todos) > Ptemplates > P todos > file (.html)

</br>

## Renderizar um arquivo html
dentro de:

todos > views

```
from django.shortcuts import render

def home(request):
    return render(request, "todos/home.html")
```
e informar dentro das URLS do app

dentro de:
setup > url 
```
from todos.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
```

e após: 
```
python manage.py runserver
```
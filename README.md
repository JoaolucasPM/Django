# Criando as rotas list e form

### Após ter criado uma model, pode-se usar html para renderizar esses dados no front end

## 1 - Fazer a imortação do banco no arquivo de `views.py`

```
from .models import Todo
```

Todo = o nome do objeto dentro do `models.py`

## 2 - Exibir dados (GET)

### Django já tem classes pré-contruidas ou genéricas dentro do arquivo `views.py` faremos essa importação, e usaremos o 'ListView' para fazer a listagem

```
from django.views.generic import ListView
```

## Criar o objeto que receba o ListView o banco, a pagina e o nome do objeto

```
class ProductListView(ListView):
    model = Todos
    template_name = 'todos/list.html'
    context_object_name = 'listP'
```

### E dentro do `urls.py` alterar as configuração do rota, indicando que será usada templates genéricos

```
path('list/',ProductListView.as_view(), name='list')
```

### E dentro do `list.html` usar as tags de `{ % for % }` `{% endfor %}`

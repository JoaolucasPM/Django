# Criando rota para inserir dados (POST)

## Passos para configurar e usar o Crispy Forms no Django:

```
pip install django-crispy-forms
```

ou

```
pip install crispy-bootstrap5
```

### Adicionar Crispy Forms nas configurações do Django Agora, adicione 'crispy_forms' e o pacote de bootstrap (ou o framework que você escolher) no arquivo settings.py:

```
INSTALLED_APPS = [
    # Outros apps
    'crispy_forms',
    'crispy_bootstrap5',  # Se você estiver usando Bootstrap 5
]

# Define o template pack que você vai usar (Bootstrap 5 neste exemplo)
CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

E dentro do arquivo `todo_form.html`

```
<form method="POST">
  {% csrf_token %} {{form | crispy}}

  <button type="submit" class="btn btn-primary">Salvar</button>
</form>
{% endblock content %}
```

## Importar view gerencias dessa vez a `CreateView` dentro de **`Views.py`** e o reverse_lazy pra quando houver sucesso na pagina.

```
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


class ProductCreateView(CreateView):
    model = Todos
    template_name = 'todos/form.html'  
    fields = ["nome", "cidade"] #Campos que aparecerão
    success_url = reverse_lazy("list")

```
## Detro do arquivo `urls.py` configurar o nome da rota 

```
from todos.views import home, ProductListView, ProductCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', ProductCreateView.as_view(), name='form'),
    path('list/',ProductListView.as_view(), name='list'),

]
```
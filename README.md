# Navegação entre paginas

## 1 - Nomear uma url com o **`name`**:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),

]
```

## e dentro da ancora inserir a tag

**`{ url }`** e o nome da função criada **`{ url form }`**

```
 <a href="{% url "form" %}" class="btn btn-primary">Login</a>

```

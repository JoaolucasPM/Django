# Criando um model

## 2 - Criar um modelo que é um objeto no banco de dados

```
class Todos(models.Model):
    nome =   models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
```

### para criar tabela no banco de dados

**`python manage.py makemigrations`**

### Depois para aplicar a migração

**`python manage.py migrate`**

# Acessando a area admin do django

### python manage.py createsuperuser

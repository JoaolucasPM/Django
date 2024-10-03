from django.db import models
class Todos(models.Model):
    nome =   models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)

# Usando arquivos staticos com django

<h2>1 - Criar um diretorico chamado 'static' dentro do aplicação:</h2>

### Caminho das pastas
- todos > static
- todos > static > todos > css
- todos > static > todos > css > file style.css

<h2>2 - Dentro do  settings.py  </h2>

```
 STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  
]
```

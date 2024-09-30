# Trabalhando com extends

### No Django, o sistema de templates é projetado para reutilizar partes do layout HTML, tornando o desenvolvimento mais eficiente e organizado. O uso do **`extends`** é uma das principais formas de fazer isso.

<br/>

## 2 - Primeiro passo:

### Criar o esqueleto do projeto **`base.html`**

- Cabeçalho (Uma para todos)
- Menu (Um para cada pagina)
- Rodapé (Um para todos)

### A logica é aproveitar o reaproveitar todo o Cabeçalho e Rodapé, alterando apenas o Menu.

<br/>

## 3 - Usando as tags **`extends`**, **`block`** e **`endblock`**

### Aonde teremos conteudos que vão mudar, adcionaremos a tag **`block`** e **`endblock`** juntos ao nome desse "bloco".

No exemplo abaixo foi usado dentro do **`main`**:

```
    <main>
      {% block content %}

      {% endblock %}
    </main>
```
## E onde vamos aproveitar aquilo que está dentro do **`base.html`** (header e footer) usamos usamos a tag **`extends`** junto a origem herdada.

```  
{% extends "base.html" %}
```
(Aqui já estará rendizando na tela o html base)

### e após usaremos  `block`** e o **`endblock` junto a nome do bloco, alterando para o novo conteúdo.

```
{% block content %}
<form>
<h1>Novo conteudo </h2>

{% endblock content %}

```
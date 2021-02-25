# Diario
Esta é uma aplicação que tem o intúito de funcionar como um diário, onde pode-se anotar idéias e pensamentos que poderão ser
desenvolvidas posteriormente.

Esta é uma aplicação simples, que dispõe de uma pagina para listar as anotações.
![Anotações](https://github.com/josevictorp81/Diario/blob/main/imagens/anota%C3%A7%C3%B5es.png)

E uma pagina que permite adicionar mais anotações.
![Adicionar Anotação](https://github.com/josevictorp81/Diario/blob/main/imagens/nova-anota%C3%A7ao.png)

# Tecnologias
* [Django](https://www.djangoproject.com/)
#### Requisitos
* [python](https://www.python.org) instalado.

# Instalação e Execução
1. Crie um ambiente virtual
```
python -m venv venv (use python3 para linux)
```

2. Ative o ambiente virtual
```
venv/Scripts/Activate
```

3. Instale as bibliotecas do projeto
```
pip install -r requirements.txt
```

4. Cria os modelos
```
python manage.py makemigrations
```

5. Migra os modelos para o banco de dados
```
python manage.py migrate
```

6. Crie o superusuário
```
python manage.py createsuperuser
```
7. Rodando o projeto
```
python manage.py runserver
```

Acesso à homepage e o admin no navegador: 127.0.0.1:8000, 127.0.0.1:800/admin.


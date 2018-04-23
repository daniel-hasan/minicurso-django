# minicurso-django
Dinâmica do minicurso de django

## Configurando um novo projeto no Django

Crie uma pasta (Django-com-Piratas) em sua Área de Trabalho para armazenar seu código. Abra o terminal (ctrl+alt+t) e execute os
comandos:

```
   cd <desktop>
   mkdir <nome_pasta>
```
Entre na pasta criada e execute:

```
   cd <nome_pasta>
   django-admin.py startproject piratas
```
O comando django-admin.py startproject é responsável por iniciar um diretório para o seu projeto (chamado piratas) implementando
os arquivos: __ init__.py,manage.py, settings.py e urls.py

Entre na pasta piratas e execute:

```
   cd piratas
   django-admin startapp piratasapp
```
O comando django-admin startapp é responsável por criar uma aplicação. Nele será que encontrado a View, o static e os migrates. 
Como uma nova aplicação foi criada deve-se registrá-la nas configurações (settings). Para isso, vá para a pasta piratas que possui
o arquivo settings.py.
No terminal execute:

```
   gedit settings.py
```
O gedit, editor de texto, irá abrir o arquivo settings.py. Procure por “INSTALLED_APPS” e adicione  a aplicação ‘piratasapp’, ao 
final do bloco, salve e feche o arquivo.


## Configurando o Banco de Dados

Crie a tabela tesouros:

```
   sudo su
   mysql
   CREATE DATABASE tesouros CHARACTER SET utf8mb4;
```
Crie um usuário:

```
   CREATE USER 'aluno'@'127.0.0.1' IDENTIFIED BY 'django';
   GRANT ALL ON *.* TO 'aluno'@'127.0.0.1';
```
Abra novamente o arquivo de settings.py, procure por “DATABASES” e substitua tudo por:

```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tesouros',
        'USER': 'aluno',
        'PASSWORD': 'django',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CHARSET': 'utf8',
    }
  }
```
Crie a classe Tesouro em models.py:
(Fique atento a identação pois será ela a determinante de um bloco de código)

```
  class Tesouro(models.Model):
	    nome = models.CharField(max_length=45)
	    quantidade = models.IntegerField()
	    valor = models.DecimalField(max_digits=10,decimal_places=2, blank=True)
	    img_tesouro = models.ImageField(upload_to="imgs")
```
As imagens enviadas para ImageField não são armazenados no banco de dados, mas sim no sistema de arquivos. Isso significa que no banco, ImageField é criado como um campo de string, contendo a referência ao arquivo atual. Para criar o arquivo físico que ficará as imagens é necessário editar o settings (o ImageField exige que a url também seja alterada mas isso será tratado mais a frente). 

Abra o settings e adicione ao final do arquivo:

```
  gedit settings.py
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
Rode o migrate para salvar as modificações efetuadas até o momento no models:
(O arquivo manage.py se encontra em Django-com-Piratas/piratas)

```
  python3 manage.py makemigrations
  python3 manage.py migrate
```
### Usando o admin do django

Para criar um usuário para usar a interface do admin do django, no terminal insira: 

```
  python3 manage.py createsuperuser;
```
Para adicionar o Banco de Dados a Interface do Admin abra o arquivo admin.py que se encontra no diretório piratasapp e registre o banco:

```
  gedit admin.py
```

```
  from piratapp.models import Tesouro

  admin.site.register(Tesouro)
```

## Criando um Template

Para armazenar os arquivos dinâmicos (no caso deste minicurso o html), crie uma pasta chamada  templates no diretório (Django-com-Piratas/piratas). 
No terminal crie a pasta:

```
  mkdir templates
```
No arquivo settings.py, em  TEMPLATES, modifique 'DIRS':

```
  'DIRS': [os.path.join(BASE_DIR, 'templates')],
```
Com o diretório criado, crie um arquivo na pasta templates chamado index.html e adicione o html disponibilizado.

```
<O código será disponibilizado aqui>
```

## Adicionando Arquivos Estáticos

Para armazenar os arquivos estáticos (no caso deste minicurso o CSS e ícones) crie uma pasta chamada  static no diretório da aplicação (Django-com-Piratas/piratas/app). 
No terminal digite:

```
  mkdir static
```
Entre novamente no arquivo settings e adicione ao final:

```
  STATIC_URL = '/static/'
```
Dentro da pasta static, crie duas pastas chamadas imgs e css:

```
  mkdir imgs
  mkdir css
```
Em imgs salve as imagens disponibilizadas no repositório.
Em css crie um arquivo chamado estilos.css e adicione o CSS disponibilizado: 

```
  h1 {
   	  margin-top: 0;
          color: gold;
          text-shadow: 2px 2px black;
  }

  body {
  	 background-image: url(../imgs/fundo-da-ilha-pirata.jpg);
         background-repeat: no-repeat;
         background-position: left bottom;
         background-size: cover;
         height: 100%;
         text-align: center;
         margin: 0% 25%;
  }

  html {
  	 text-align: center;
         height: 100%;
  }


  table {
         margin-left: auto;
         margin-right: auto;
         border-collapse: collapse;
         background: white;
  }

  caption, p {
         background-color: rgba(255, 255, 255, .7);
         font-size: 95%;
  }

  td, th {
  	 padding: 4px 8px;
  }

  th, #bot {
         border-top: 1px solid black;
         border-bottom: 1px solid black;
         margin-collapse: collapse;
  }

  th {
         background-color: green;
         border-color: black;
  }

  #bot {
         background-color: orange;
         border-color: black;
  }
```

## Criando a View

A view é responsável por solicitar informações do models e passá-las para um template por isso se torna necessário a criação de uma classe view para a visualização

<continua>
  
## Vinculando o Template a uma VIew - URLs

Para vincular uma View a um Template é necessário criar uma url. Para isso, abra o arquivo urls.py que se encontra em (Django-com-Piratas/piratas/piratas):

Importe a View e a url:

```
  from django.conf.urls import url
  from app import views
```
<continua>
  
# Navegando em arquivos no terminal

Para entrar em uma pasta seguinte;
```
  cd <nome_pasta>
```
Para voltar para a pasta anterior;
```
  cd ..
```
Para voltar tudo de uma vez;
```
  cd ~
```
Para ver os conteúdos da pasta;
```
  ls
```


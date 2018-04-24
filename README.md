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
<!DOCTYPE html>
    <head>
        <link rel="icon" href="">
        <title>Gerenciador de Tesouros</title>
        <meta charset="UTF-8">
    	<link rel="stylesheet" type="text/css" href="">
	<script>let valorTotal; let None; let soma=0;</script>
    </head>
    <body>
        <h1>Gerenciador de Tesouros</h1>

	<div id="myModal" class="modal">

	  <div class="modal-content">
	    <span class="close">&times;</span>
		<form action="" method="post" enctype="multipart/form-data">
		    
		    <input type="submit" value="Adicionar" />
		</form>
	  </div>

	</div>

	<button id="myBtn">Adicionar</button><p>

        <table>
            <caption>Estes são os tesouros acumulados do
            Barba-Ruiva em suas aventuras</caption>
            <thead>
                <tr>
                    <th>Tesouro</th>
                    <th>Nome</th>
                    <th>Valor unitário</th>
                    <th>Quantidade</th>
                    <th>Valor total</th> 
		    <th colspan="2">Editar</th>
                </tr>
            </thead>
	    <tbody>
		
	    
		<tr>
		     <td></td>
		     <td></td>
		     <td></td>
		     <td></td>
		     <td id="" class="valorTotal">
			<script> 
				if(){
					valorTotal =  * ;
				} else {
					valorTotal = "-";
				}
				document.querySelector("#id"+"").innerHTML = valorTotal;
				console.log(valorTotal);
			</script>
		     </td>
		     <td><form action="" method="post">{% csrf_token %}
	         		<button id="delete">Remover</button>
	         	</form></td>
		     <td><button data-nome="{{ objTesouro.nome }}" class="update">Modificar</button></td>
		</tr>
	    
	    </tbody>
            <tfoot>
                <tr>
                    <td colspan="4" id="bot">Total</td>
                    <td id="bot" class="soma">
			<script> 
				
				if(){
						soma +=  * ;
					}
				
				document.querySelector(".soma").innerHTML = soma;
				console.log(soma);
			</script>
		    </td>
		    <td colspan="2" id="bot"></td>
                </tr>
            </tfoot>
        </table>
        <p>Yarr Harr, marujo! Aqui é o temido
        Barba-Ruiva e você deve me ajudar a
        contabilizar os espólios das minhas
        aventuras!
        </p>
	
	<script>		
	
	function initModal(idModal, idBotao){
		var modal = document.getElementById(idModal);
		var btn = document.getElementById(idBotao);
		var span = document.getElementsByClassName("close")[0];
		
		span.addEventListener("click", function() {
		    modal.style.display = "none";
		});
		if(idBotao != ""){
			btn.onclick = function() {
			    modal.style.display = "block";
			}
		}
		
		window.addEventListener("click", function(event) {
		    if (event.target == modal) {
			modal.style.display = "none";
		    }
		});
	}
	
	
	initModal("myModal", "myBtn");
	
	{% if object.id %}
		document.getElementById("myModal").style.display = "block";
		
	{% endif %}
	var arrBtnUpdate = document.querySelectorAll(".update");
	for(var i =0 ; i<arrBtnUpdate.length ; i++){	
		arrBtnUpdate[i].addEventListener("click", function(e) {
			    var btnTesouro = e.currentTarget;
			    window.location.href = "{% url 'TesouroUpdate' ''%}"+btnTesouro.dataset.nome;
			});
	}
	
	</script>
	
    </body>
</html>
```

Adicione a tag responsável por carregar os arquivos estáticos no template:

```
{% load static %}
```

Para adicionar o diretório de arquivos estáticos o django dispoe da tag {% static 'caminho_static'%} 

Adicione o ícone da página:

```
{% static 'imgs/calice.ico'%}
```
Adicione o css da página:

```
{% static 'css/estilos.css'%}
```
Para criar um formulário usando generic view o django fornece a tag form.as_p que gera o formulário de acordo com os fields definidos na view. Adicione a tag para gerar a view de inserção/atualização:

```
{{ form.as_p }}
```
Cross Site Request Forgery protection é usada para proteção. Adicione ao form:

```
{% csrf_token %}
```
Para criar a tabela dinamicamente é necessário percorrer os dados no banco. Para isso crie um for: 
```
{% for objTesouro in lista_tesouro %}
{% endfor %}
```

```
		     <td><img src="{{ MEDIA_URL }}{{ objTesouro.img_tesouro }}"/></td>
		     <td>{{ objTesouro.nome }}</td>
		     <td>{{ objTesouro.valor }}</td>
		     <td>{{ objTesouro.quantidade }}</td>
		     <td id="id{{ objTesouro.id }}" class="valorTotal">
```
```
	<td id="id{{ objTesouro.id }}" class="valorTotal">
			<script> 
				if({{ objTesouro.valor }}){
					valorTotal = {{ objTesouro.valor }} * {{ objTesouro.quantidade }};
				} else {
					valorTotal = "-";
				}
				document.querySelector("#id"+"{{ objTesouro.id }}").innerHTML = valorTotal;
				console.log(valorTotal);
			</script>
```
URL: 
```
{% url 'TesouroDelete' objTesouro.nome %}
```
```
				{% for objTesouro in lista_tesouro %}
					if({{ objTesouro.valor }}){
						soma += {{ objTesouro.valor }} * {{ objTesouro.quantidade }};
					}
				{% endfor %}
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
  
  /* Modal retirado https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_modal */

.modal {
    display: none;
    position: fixed; 
    z-index: 1; 
    padding-top: 100px; 
    left: 0;
    top: 0;
    width: 100%; 
    height: 100%;
    overflow: auto;
    background-color: rgb(0,0,0); 
    background-color: rgba(0,0,0,0.4);
}

.modal-content {
    background-color: #fefefe;
    margin: auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
}

.close {
    color: #aaaaaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: #000;
    text-decoration: none;
    cursor: pointer;
}
```

## Criando a View

A view é responsável por solicitar informações do models e passá-las para um template por isso se torna necessário a criação de uma classe view para a visualização.

No arquivo views.py, adicione:

```
from django.shortcuts import render
from django.forms.utils import ErrorList
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from piratapp.models import Tesouro
from django.urls.base import reverse, reverse_lazy

class FormValidation(object):

    def form_valid(self, view, form):
        lsta_tesouro = Tesouro.objects.filter(nome=form.instance.nome)
        if(form.instance.pk != None):
            lsta_tesouro = lsta_tesouro.exclude(pk=form.instance.pk)
        if len(lsta_tesouro) > 0:
            errors = form._errors.setdefault("nome", ErrorList())
            errors.append(u"nomes iguais não são permitidos")
            return False
        
        return True

class TesouroInsert(CreateView):
    
    model = Tesouro
    template_name = "index.html"
    form_validator = FormValidation()

    fields=["img_tesouro", "nome", "valor", "quantidade"]
	
    def form_valid(self, form):
        bol_valid = TesouroInsert.form_validator.form_valid(self, form)
        return super(CreateView, self).form_valid(form) if bol_valid else super(CreateView, self).form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super(TesouroInsert, self).get_context_data(**kwargs)
        context["lista_tesouro"] = Tesouro.objects.all()

        return context  

    def get_success_url(self):
        return reverse('GerenciadorTesouros')
    
    class Meta:
        labels = {
            "img_tesouro" : "Tesouro",
            "nome" : "Nome",
            "valor" : "Valor unitário",
            "quantidade" : "Quantidade"
        } 

class TesouroUpdate(UpdateView):
    model = Tesouro
    template_name = "index.html"
    form_validator = FormValidation()

    fields=["img_tesouro", "nome", "valor", "quantidade"]
	
    def form_valid(self, form):        
        bol_valid = TesouroUpdate.form_validator.form_valid(self, form)
        return super(UpdateView, self).form_valid(form) if bol_valid else super(UpdateView, self).form_invalid(form)
    
    def get_object(self):
        return Tesouro.objects.get(nome=self.kwargs["nome"])
    
    def get_success_url(self):
        return reverse('GerenciadorTesouros')
    
class TesouroDelete(DeleteView):
    model = Tesouro

    def get_object(self):
        return Tesouro.objects.get(nome=self.kwargs["nome"])
     
    def get_success_url(self):
	return reverse_lazy('GerenciadorTesouros')
```

## Vinculando o Template a uma VIew - URLs

Para vincular uma View a um Template é necessário criar uma url. Para isso, abra o arquivo urls.py que se encontra em (Django-com-Piratas/piratas/piratas):

Importe a View, a url e o static:

```
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from piratapp import views
from django.conf import settings
from django.conf.urls.static import static
```
Crie uma url para a view de visualização/inserção:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^GerenciadorTesouros$', views.TesouroInsert.as_view(), name='GerenciadorTesouros'),
    url(r'^GerenciadorTesouros/Update/(?P<nome>.*)$', views.TesouroUpdate.as_view(), name='TesouroUpdate'),
    url(r'^GerenciadorTesouros/(?P<nome>.*)$', views.TesouroDelete.as_view(), name='TesouroDelete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```  

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


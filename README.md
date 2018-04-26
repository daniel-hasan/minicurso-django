# minicurso-django
Dinâmica do minicurso de django

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

## Como foi configurado um novo projeto no Django

Na Área de Trabalho foi aberto o terminal (ctrl+alt+t) e executado o comando:

```
  django-admin.py startproject piratas
```
O comando django-admin.py startproject é responsável por iniciar um diretório para o seu projeto (chamado piratas) implementando
os arquivos: __ init__.py,manage.py, settings.py e urls.py

Na pasta piratas foi executado:

```
   cd piratas
   django-admin startapp piratasapp
```
O comando django-admin startapp é responsável por criar uma aplicação. Nele será que encontrado a View, o static e os migrates. 
Como uma nova aplicação foi criada deve-se registrá-la nas configurações (settings). Para isso, na pasta piratas que possui
o arquivo settings.py a linha do “INSTALLED_APPS” foi modificada adicionando o ‘piratasapp’, ao final do bloco no arquivo.


## Como foi configurado o Banco de Dados

No arquivo models.py encontrado no piratasapp foi criada a classe Tesouro:
(Fique atento a identação pois será ela a determinante de um bloco de código)

```
  class Tesouro(models.Model):
	    nome = models.CharField(max_length=45)
	    quantidade = models.IntegerField()
	    valor = models.DecimalField(max_digits=10,decimal_places=2, blank=True)
	    img_tesouro = models.ImageField(upload_to="imgs")
```
Atenção: As imagens enviadas para ImageField não são armazenados no banco de dados, mas sim no sistema de arquivos. Isso significa que no banco, ImageField é criado como um campo de string, contendo a referência ao arquivo atual. Para criar o arquivo físico que ficará as imagens foi necessário editar o settings (o ImageField exige que a url também seja alterada mas isso será tratado mais a frente). 
Em settings foi adicionado ao final do arquivo:

```
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
O migrate foi rodado para salvar as modificações efetuadas até o momento no models:
(O arquivo manage.py se encontra em piratas)

```
  python3 manage.py makemigrations
  python3 manage.py migrate
```
Para adicionar o Banco de Dados a Interface do Admin que será introduzida na prática foi necessário editar o arquivo admin.py que se encontra no diretório piratasapp e registrando o banco:

```
  from piratapp.models import Tesouro

  admin.site.register(Tesouro)
```

## Como foi configurado o Template

Para armazenar os arquivos dinâmicos (no caso deste minicurso o html), foi criado uma pasta chamada  templates no diretório (piratas). 
No arquivo settings.py, em  TEMPLATES, foi modificado o 'DIRS':

```
  'DIRS': [os.path.join(BASE_DIR, 'templates')],
```
Com o diretório criado, foi deixado um arquivo na pasta templates chamado index.html com o html semipronto para editá-lo na prática

## Como foi adicionado Arquivos Estáticos

Para armazenar os arquivos estáticos (no caso deste minicurso o CSS e ícones) foi criado uma pasta chamada  static no diretório da aplicação (piratas/piratasapp).
Dentro da pasta static, foi criado duas pastas chamadas imgs e css:
Em imgs foi adicionado as imagens de fundo e ícone.
Em css foi adicionado o arquivo estilos.css. 


## Como foi configurada a View

No arquivo views.py, foram adicionada as seguintes importações que serão necessárias para a implementação do código do minicurso, o metódo get_context_data e a classe de validação de formulário:

```
from django.shortcuts import render
from django.forms.utils import ErrorList
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from piratapp.models import Tesouro
from django.urls.base import reverse, reverse_lazy
'''
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
    
    def get_context_data(self, **kwargs):
        context = super(TesouroInsert, self).get_context_data(**kwargs)
        lstTesouros = Tesouro.objects.annotate(total=ExpressionWrapper(F('valor') * F('quantidade'),output_field=DecimalField(max_digits=10,decimal_places=2, blank=True)))
        context["lista_tesouro"] = lstTesouros
        soma = 0
        for tesouro in lstTesouros:
            soma += tesouro.total
        context["preco_total"] = soma
        return context  

        return context  
'''
# class TesouroUpdate(UpdateView):
    
# class TesouroDelete(DeleteView):
  
```

## Como foi configurada a URL

Foram necessária as seguintes importações para a url

```
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from piratapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```  

# A pática está no slide e após o fim do minicurso será disponibilizada aqui

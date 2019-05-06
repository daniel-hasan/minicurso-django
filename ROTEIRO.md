# Gerenciador de Tesouros

## Instalação dos requisitos para a prática
  1. Abra o terminal (Ctrl+Alt+t).
  2. Digite os seguintes comandos:
    ```
    sudo apt install mysql-server mysql-client
    sudo apt install python3 python3-pip
    sudo apt install libmysqlclient-deve
    pip3 install django
    ```

## Roteiro da prática

  1. [Baixe o repositório](https://github.com/brandaogabriel7/minicurso-django/archive/master.zip) e extraia os arquivos.

  2. Abra o terminal e navegue até minicurso-django/piratas utilizando o comando `cd`

  3. Execute `python3 manage.py runserver` e abra https://127.0.0.1 em um navegador. Você deve observar uma página com erro 404. Isso aconteceu porque nosso projeto ainda não tem nenhuma url definida.

  4. Agora você irá criar um super usuário para ter acesso ao painel de gerenciamento do BD. Abra outra janela do terminal (Ctrl+Shift+t). Digite o comando `python3 manage.py createsuperuser` e preencha o necessário. Agora abra https://127.0.0.1:8000/admin. Ao efetuar o login aparecerá o painel de gerenciamento da aplicação.

  5. Agora nós iremos alterar o template. Abra o arquivo index.html e altere-o de acordo com o trecho abaixo:
  ```html
      <!DOCTYPE html>
      {% load static %}
      <head>
          <link rel="icon" href="{% static 'imgs/calice.ico' %}">
          <title>Gerenciador de Tesouros</title>
          <meta charset="UTF-8">
          <link rel="stylesheet" type="text/css" href="{% static 'css/estilos.css' %}">
      </head>
      <body>
          <h1>Gerenciador de Tesouros</h1>

      <div id="myModal" class="modal">

        <div class="modal-content">
          <span class="close">&times;</span>
          <form action="" method="post" enctype="multipart/form-data">{% csrf_token %}
              {{ form.as_p }}
              <input type="submit" value="Adicionar" />
          </form>
        </div>

      </div>

      [...]
  ```
  6. Seguindo, nós alteraremos a view para realizar a operação de adicionar um tesouro à tabela. Insira o seguinte escopo para a View TesouroInsert:
    ```python
    class TesouroInsert(CreateView):

        model = Tesouro
        template_name = "index.html"
        util = TesouroUtil()

        fields = ["img_tesouro", "nome", "valor", "quantidade"]

        def form_valid(self, form):
            bol_valid = TesouroInsert.util.form_valid(self, form)
            return super(CreateView, self).form_valid(form) if bol_valid else super(CreateView, self).form_invalid(form)

        def get_context_data(self, **kwargs):
            context = super(TesouroInsert, self).get_context_data(**kwargs)
            TesouroInsert.util.get_context_data(context)
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
    ```

  7. Para finalizar, insira a URL correspondente a essa view no array do arquivo *urls.py*:
    ```python
    url(r'^GerenciadorTesouros$', views.TesouroInsert.as_view(), name='GerenciadorTesouros')
    ```  

  8. Modifique o template novamente para finalizar a tabela dinâmica:
    ```html
    <tbody>
        {% for objTesouro in lista_tesouro %}
		<tr>
		     <td><img src="{{ objTesouro.img_tesouro.url }}"/></td>
		     <td>{{ objTesouro.nome }}</td>
		     <td>{{ objTesouro.valor }}</td>
		     <td>{{ objTesouro.quantidade }}</td>
		     <td>{{ objTesouro.total }}</td>
		     <td>
			<form action="" method="post">
	         		<button id="delete">Remover</button>
	         	</form>
		     </td>
		     <td><button data-nome="{{ objTesouro.nome }}" class="update">Modificar</button></td>
		</tr>
        {% endfor %}
	</tbody>
    ```

  >Neste ponto da prática, você já deve conseguir adicionar tesouros novos à tabela em https://127.0.0.1/GerenciadorTesouros

  9. Agora nós vamos adicionar as views de Update e Delete.
    ```python
    class TesouroUpdate(UpdateView):
        model = Tesouro
        template_name = "index.html"
        util = TesouroUtil()

        fields = ["img_tesouro", "nome", "valor", "quantidade"]

        def form_valid(self, form):
            bol_valid = TesouroUpdate.util.form_valid(self, form)
            return super(UpdateView, self).form_valid(form) if bol_valid else super(UpdateView, self).form_invalid(form)

        def get_context_data(self, **kwargs):
            context = super(TesouroUpdate, self).get_context_data(**kwargs)
            TesouroUpdate.util.get_context_data(context)
            return context

        def get_object(self):
            return Tesouro.objects.get(nome=self.kwargs["nome"])

        def get_success_url(self):
            return reverse('GerenciadorTesouros')

    ```
    ```python
    class TesouroDelete(DeleteView):
        model = Tesouro

        def get_object(self):
            return Tesouro.objects.get(nome=self.kwargs["nome"])

        def get_success_url(self):
            return reverse_lazy('GerenciadorTesouros')
    ```

  10. Agora falta adicionar as urls de *Update* e *Insert*. O arquivo de urls vai ficar assim:
    ```python
    from django.contrib import admin
    from django.urls import path
    from django.conf.urls import url
    from piratasapp import views
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        url(r'^GerenciadorTesouros$', views.TesouroInsert.as_view(), name='GerenciadorTesouros'),
        url(r'^GerenciadorTesouros/Update/(?P<nome>.*)$', views.TesouroUpdate.as_view(), name='TesouroUpdate'),
        url(r'^GerenciadorTesouros/(?P<nome>.*)$', views.TesouroDelete.as_view(), name='TesouroDelete'),
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

  11. Volte ao template para mudar o botão de remoção:
    ```html
    <form action="{% url 'TesouroDelete' objTesouro.nome %}" method="post">{% csrf_token %}
            <button id="delete">Remover</button>
     </form>
    ```

  12. Para finalizar, altere o script presente no template para atualização de tesouros:
    ```Javascript
    initModal("myModal", "myBtn");
    {% if object.id or form.errors %}
        document.getElementById("myModal").style.display = "block";
    {% endif %}
    var arrBtnUpdate = document.querySelectorAll(".update");
    for(var i =0 ; i<arrBtnUpdate.length ; i++){
        arrBtnUpdate[i].addEventListener("click", function(e) {
                var btnTesouro = e.currentTarget;
                window.location.href = "{% url 'TesouroUpdate' ''%}"+btnTesouro.dataset.nome;
            });
    }
    ```
> A este ponto o seu gerenciador de tesouros deve estar funcionando. Caso tenha alguma dúvida, sinta-se a vontade para perguntar.

## FAQ
  * Pode acontecer algum erro de permissão ao executar os comandos do Python. Para corrigir bastar adicionar sudo ao início do comando.
  * A ordem das urls pode afetar o funcionamento da aplicação. Certifique-se de seguir estritamente a ordem apresentada acima.

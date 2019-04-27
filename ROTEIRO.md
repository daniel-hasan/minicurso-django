# Gerenciador de Tesouros

## Roteiro da prática

  1. [Baixe o repositório](https://github.com/brandaogabriel7/minicurso-django/archive/master.zip) e extraia os arquivos.

  2. Abra o terminal e navegue até minicurso-django/piratas utilizando o comando `cd`

  3. Abra outra janela do Terminal(Ctrl+shift+t) e execute `python3 manage.py runserver`. Preencha o necessário e abra [127.0.0.1:8000/admin]. Ao efetuar o login aparecerá o painel de gerenciamento.

  4. Feche a página e desligue o servidor(Ctrl+C no terminal executando o servidor).

  5. Abra o arquivo index.html e altere-o de acordo com o trecho abaixo:
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
  ```
  6. Insira o seguinte escopo para a View TesouroInsert:
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

  7. Insira a URL correspondente a esta view no array do arquivo *urls.py*:
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

  9. Execute o servidor e verifique que [o site](127.0.0.1:8000/GerenciadorTesouros) já permite adicionar tesouros à tabela.

  10. Agora nós vamos adicionar as views de Update e Delete.
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

  11. Adicione suas URLs correspondentes ao arquivo urls.py:
    ```python
    url(r'^GerenciadorTesouros/(?P<nome>.*)$', views.TesouroDelete.as_view(),
name='TesouroDelete')
    ```

    ```python
    url(r'^GerenciadorTesouros/Update/(?P<nome>.*)$', views.TesouroUpdate.as_view(),
name='TesouroUpdate')
    ```

  12. Volte ao template para mudar o botão de remoção:
    ```html
    <form action="{% url 'TesouroDelete' objTesouro.nome %}" method="post">{% csrf_token %}
            <button id="delete">Remover</button>
     </form>
    ```

  13. Para finalizar, altere o script presente no template para atualização de tesouros:
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

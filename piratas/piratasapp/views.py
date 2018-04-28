from django.shortcuts import render
from django.forms.utils import ErrorList
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from piratapp.models import Tesouro
from django.urls.base import reverse, reverse_lazy
from django.db.models import F,ExpressionWrapper,DecimalField
'''
class TesouroUtil(object):

    def form_valid(self, view, form):
        lsta_tesouro = Tesouro.objects.filter(nome=form.instance.nome)
        if(form.instance.pk != None):
            lsta_tesouro = lsta_tesouro.exclude(pk=form.instance.pk)
        if len(lsta_tesouro) > 0:
            errors = form._errors.setdefault("nome", ErrorList())
            errors.append(u"nomes iguais não são permitidos")
            return False
        
        return True

    def get_context_data(self, context):
        lstTesouros = Tesouro.objects.annotate(total=ExpressionWrapper(F('valor') * F('quantidade'),output_field=DecimalField(max_digits=10,decimal_places=2, blank=True)))
        context["lista_tesouro"] = lstTesouros
        soma = 0
        for tesouro in lstTesouros:
            soma += tesouro.total
        context["preco_total"] = soma 
'''      

#class TesouroInsert(CreateView):
 
#class TesouroUpdate(UpdateView):
    
#class TesouroDelete(DeleteView):
   

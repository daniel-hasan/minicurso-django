from django.db import models

class Tesouro(models.Model):
    nome = models.CharField(max_length=45)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    img_tesouro = models.ImageField(upload_to="imgs")

    def __str__(self):
        return self.nome+" quantidade: "+str(self.quantidade)+" R$ "+str(self.valor)+" "+str(self.img_tesouro)

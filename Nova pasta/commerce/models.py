from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    preco = models.FloatField()
    descricao = models.CharField(max_length=250, null=True)
    imagem = models.ImageField(upload_to='imagem')

    def __str__(self):
        return self.nome
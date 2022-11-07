from django.db import models

#Cada class será uma tabela, especificado pelo models.Model, no banco de dados
class Empresa(models.Model):
    nome = models.CharField(max_length=30) #coluna da tabela
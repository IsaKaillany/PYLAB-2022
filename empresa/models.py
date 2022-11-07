from django.db import models

class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

#Cada class será uma tabela, especificado pelo models.Model, no banco de dados
class Empresa(models.Model):
    choices_nicho_mercado = (
        ('M', 'Marketing'), #n números de char que representam alguma coisa
        ('N', 'Nutrição'),
        ('D', 'Design')
    )
    logo = models.ImageField(upload_to="logo_empresa", null=True)
    nome = models.CharField(max_length=30) #coluna da tabela
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    tecnologias = models.ManyToManyField(Tecnologias)
    endereco = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()
    nicho_mercado = models.CharField(max_length=3, choices=choices_nicho_mercado)

    def __str__(self):
        return self.nome

class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )
    
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(Tecnologias, related_name='estudar')


    def __str__(self):
        return self.titulo
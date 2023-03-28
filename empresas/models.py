from django.db import models


class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

class Empresa(models.Model):

    choices_size = (
        ('Pequena', 'Até 10 pessoas'),
        ('Média', 'Até 100 pessoas'),
        ('Grande', 'Mais de 1000 pessoas'),
    )
    choices_niche = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design'),
    )

    logo = models.ImageField(upload_to='logo_empresa')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    headquarters = models.CharField(max_length=30)
    technologies = models.ManyToManyField(Tecnologias)
    marketing_niche = models.CharField(max_length=3, choices=choices_niche)
    specifications = models.TextField()

    def __str__(self) -> str:
        return self.nome
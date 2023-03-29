from django.db import models


class Technologies(models.Model):
    technology = models.CharField(max_length=30)

    def __str__(self):
        return self.technology

class Specializations(models.Model):
    specialization = models.CharField(max_length=30)

    def __str__(self):
        return self.specialization

class Company(models.Model):

    choices_size = (
        ('Micro', 'Até 19 colaboradores'),
        ('Pequena', '20 à 99 colaboradores'),
        ('Media', '100 à 499 colaboradores'),
        ('Grande', 'Acima de 500 colaboradores'),
    )
    choices_niche = (
        ('M', 'Marketing'),
        ('T', 'Tecnologia'),
        ('N', 'Nutrição'),
        ('D', 'Design'),
    )

    logo = models.ImageField(upload_to='logo_empresa')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    headquarters = models.CharField(max_length=30)
    technologies = models.ManyToManyField(Technologies)
    marketing_niche = models.CharField(max_length=3, choices=choices_niche)
    specializations = models.ManyToManyField(Specializations)

    def __str__(self) -> str:
        return self.nome

class Jobs(models.Model):
    choices_experience = (
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
    
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=30)
    experience = models.CharField(max_length=2, choices=choices_experience)
    final_date = models.DateField()
    position_type = models.TimeField()
    status = models.CharField(max_length=30, choices=choices_status)
    technologies_mastered = models.ManyToManyField(Technologies)
    technologies_study = models.ManyToManyField(Technologies, related_name='estudar')


    def __str__(self):
        return self.titulo
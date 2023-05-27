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

    def qtd_vagas(self):
        return Jobs.objects.filter(company__id=self.id).count()

    choices_size = (
        ('Micro', 'Até 19 colaboradores'),
        ('Pequena', '20 à 99 colaboradores'),
        ('Media', '100 à 499 colaboradores'),
        ('Grande', 'Acima de 500 colaboradores')
    )
    choices_niche = (
        ('M', 'Marketing'),
        ('T', 'Tecnologia'),
        ('N', 'Nutrição'),
        ('D', 'Design')
    )

    name = models.CharField(max_length=50)
    email = models.EmailField()
    headquarters = models.CharField(max_length=30)
    company_size = models.CharField(max_length=30, choices= choices_size)
    marketing_niche = models.CharField(max_length=3, choices=choices_niche)
    technologies = models.ManyToManyField(Technologies)
    specializations = models.ManyToManyField(Specializations)
    logo = models.ImageField(upload_to='company_logo')

    def __str__(self) -> str:
        return self.name

class Jobs(models.Model):

    def progress(self):
        x = [((i+1)*20,j[0]) for i, j in enumerate(self.choices_status)]
        x = list(filter(lambda x: x[1] == self.status, x))[0][0]
        return x

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
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    url = models.URLField(max_length=300)
    experience = models.CharField(max_length=20, choices=choices_experience)
    final_date = models.DateField()
    position_type = models.IntegerField()
    status = models.CharField(max_length=30, choices=choices_status)


    def __str__(self):
        return self.title
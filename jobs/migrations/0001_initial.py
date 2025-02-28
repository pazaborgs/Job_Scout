# Generated by Django 4.1.7 on 2025-02-09 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('priority', models.CharField(choices=[('B', 'Baixa'), ('A', 'Alta'), ('U', 'Urgente')], max_length=1)),
                ('date', models.DateField()),
                ('finished', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.jobs')),
            ],
        ),
    ]

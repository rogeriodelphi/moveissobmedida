# Generated by Django 3.1.7 on 2021-03-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moveis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('cor', models.CharField(max_length=40, verbose_name='Cor')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor R$')),
                ('situacao', models.CharField(choices=[('NO', 'Novo'), ('US', 'Usado'), ('CD', 'Com Defeito')], max_length=2, verbose_name='Situação')),
                ('categoria', models.CharField(choices=[('RE', 'Residencial'), ('EC', 'Escritório'), ('HO', 'Home-office'), ('ES', 'Estudante')], max_length=2, verbose_name='Situação')),
            ],
        ),
    ]

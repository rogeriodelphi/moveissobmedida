# Generated by Django 3.1.7 on 2021-03-11 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moveis', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Moveis',
            new_name='Movel',
        ),
        migrations.AlterModelOptions(
            name='movel',
            options={'managed': True, 'ordering': ['nome'], 'verbose_name': 'Móvel', 'verbose_name_plural': 'Móveis'},
        ),
        migrations.AlterModelTable(
            name='movel',
            table='Movel',
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome_categoria',
            field=models.CharField(max_length=50, verbose_name='Categoria'),
        ),
    ]
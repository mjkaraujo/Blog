# Generated by Django 4.0.6 on 2022-08-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_autor_post_alter_post_categoria_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerto_post',
            field=models.TextField(verbose_name='excerto'),
        ),
    ]

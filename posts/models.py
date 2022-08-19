from ast import arg
from http.client import ImproperConnectionState
import os
from pickletools import optimize
from turtle import heading
from django.db import models
from categoria.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os

class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Titulo')
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models .DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteudo') 
    excerto_post = models .TextField(verbose_name='excerto')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem') 
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria') 
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado') 

    def __str__(self):
        return self.titulo_post

# Redimensionando a imagem salva no post
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.resize_image(self.imagem_post, 800)

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size
        new_height = round((new_width * height) / width)

        if width <= new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60,
        )
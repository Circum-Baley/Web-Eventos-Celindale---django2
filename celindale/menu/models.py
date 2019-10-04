from django.db import models


# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=30, verbose_name="Titulo")
    descripcion = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="menu")
    link = models.URLField(null=True, blank=True, verbose_name='enlace')
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualizacion")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"
        ordering = ["create"]

    def __str__(self):
        return self.title

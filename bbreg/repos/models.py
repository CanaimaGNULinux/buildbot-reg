from django.db import models


class Repositorio(models.Model):
    Nombre = models.CharField('nombre proyecto', max_length=50)
    Url = models.CharField('url repositorio del proyecto', max_length=100)

    def __unicode__(self):
        return self.Nombre

from django.db import models
from django.contrib.auth.models import User, Group

class Vendedor(models.Model):
    user = models.OneToOneField(User)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """ Override de la funcion de save para que
        al crear un vendedor, siempre se le asigne el grupo de vendedor.
        De esta forma, podemos seleccionar las vistas a las que puede acceder.
        """
        grupo_vendedor = Group.objects.get_or_create(name="vendedor")[0]
        self.user.groups.add(grupo_vendedor)
        return super(Vendedor, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Vendedores'
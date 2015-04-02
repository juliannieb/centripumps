from django.db import models
from django.contrib.auth.models import User

class Vendedor(models.Model):
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = 'Vendedores'
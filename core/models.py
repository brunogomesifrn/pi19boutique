from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	cpf = models.CharField ('CPF', max_length=11)

	def __str__(self):
		return self.email

class Tipo(models.Model):
	nome = models.CharField('Nome', max_length=100)

	def __str__(self):
		return self.nome

class Produto(models.Model):
	nome = models.CharField('Nome', max_length=100)
	valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
	foto = models.ImageField('Foto', upload_to="fotos", null=True)

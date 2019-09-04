from django.db import models

class Tipo(models.Model):
	nome = models.CharField('Nome', max_length=100)

	def __str__(self):
		return self.nome

class Produto(models.Model):
	nome = models.CharField('Nome', max_length=100)
	valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
	foto = models.ImageField('Foto', upload_to="fotos", null=True)
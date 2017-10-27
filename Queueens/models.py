from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib import admin

class Inscrito(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.EmailField(max_length=200)
	celular = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
	codigo = models.CharField(max_length=50, default='None Code')

	def inscribir(self):
		self.save()

	def __str__(self):
		return self.nombre + ' ' + self.apellido
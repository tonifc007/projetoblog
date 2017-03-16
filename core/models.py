from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	titulo = models.CharField(max_length=80, verbose_name='Título', blank=False)
	decricao = models.TextField(verbose_name='Texto', blank=False)
	data = models.DateTimeField(default=timezone.now, verbose_name='Data')

	def __str__(self):
		return self.titulo
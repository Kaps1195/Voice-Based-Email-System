from django.db import models

# Create your models here.

class Mail(models.Model):
	to = models.EmailField()
	subject = models.CharField(max_length=280)
	content = models.TextField()


	def __str__(self):
		return self.to 

		

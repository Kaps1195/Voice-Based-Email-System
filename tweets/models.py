from django.db import models

# Create your models here.
class Tweet(models.Model):
	tweets = models.TextField(max_length=140)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.tweets
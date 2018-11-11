from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=20,default='Project')
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)
	link = models.CharField(max_length=100,default='#')

	def __str__(self):
		return self.title

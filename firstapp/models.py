from django.db import models

# Create your models here.
class Slider( models.Model):

	offer= models.CharField(max_length = 100) 
	image= models.ImageField(upload_to = 'slider')
	offerDetail1= models.CharField(max_length =100)
	offerDetail2= models.CharField(max_length = 100)
	def __str__(self):
		return self.offer


class Option(models.Model):

	name = models.CharField(max_length = 100)
	detail = models. CharField(max_length = 100) 
	image = models.ImageField(upload_to = 'option')

	def __str__(self):
		return self.name

class SmallOption(models.Model):
	name = models.CharField(max_length = 100)
	detail = models.CharField(max_length = 100) 
	image = models.ImageField(upload_to = 'option')

	def __str__(self):
		return self.name

class Product(models.Model):
	Type =models.CharField(max_length = 50)
	name = models.CharField(max_length = 100)
	brand = models.CharField(max_length = 50)
	colour = models.CharField(max_length = 50) 
	desc = models.TextField()
	image = models.ImageField(upload_to = 'topproducts')
	image2 = models.ImageField(upload_to = 'topproducts')
	price = models.IntegerField()
	offerprice = models.IntegerField()
	new = models.BooleanField(default = False)
	TopProduct= models.BooleanField(default = False)
	OnSale = models.BooleanField(default =False)

	def __str__(self):
		return self.name

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null = True)
	phone = models.CharField(max_length=200, null = True)
	emai = models.CharField(max_length=200, null = True)
	profile_pic = models.ImageField(default='profile.png', null = True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200, null = True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor','Indoor'),
			('Out Door','Out Door'),
		)

	name = models.CharField(max_length=200, null = True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null = True, choices=CATEGORY)
	description = models.CharField(max_length=200, null = True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	status =(
			('Indoor','Indoor'),
			('Pending','Pending'),
			('Delivered', 'Delivered'),
		)
	# the customer field should still be there after the order has ben deleted
	customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=status)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name
	
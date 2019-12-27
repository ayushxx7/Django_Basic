from django.db import models

# Create your models here.
class user(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	email = models.EmailField(max_length=254)
	user_name = models.CharField(max_length=80)
	password = models.CharField(max_length=50)


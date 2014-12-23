from django.db import models

# Create your models here.
class List(models.Model):
	pass


class Item(models.Model):
	text = models.TextField(default = '')
	#list = models.TextField(default='') #django only saves string rep of list object, need to use a forieghn key
	list = models.ForeignKey(List,default=None)


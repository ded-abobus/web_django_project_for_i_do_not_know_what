
#не изменил (id product)

from django.db import models
from django.urls import reverse
import uuid

class ProductModel(models.Model):
	id_product = models.IntegerField(primary_key=True, help_text='Уникальный идентификатор товара')
	category = models.ForeignKey('CategoryModel', on_delete=models.SET_NULL, null=True) #id_category
	name_product = models.CharField(max_length=100)
	description = models.TextField(max_length=1000, help_text='Краткое описание товара')
	long_description = models.TextField(max_length=1500, help_text='Длинное описание товара')

	def __str__(self):
                #return self.id_product
		return f'{self.name_product} ({self.category.name_category})'

	def get_absolute_url(self):
		return reverse('index')

class CategoryModel(models.Model):
	id_category = models.IntegerField(primary_key=True, help_text='Уникальный идентификатор категории товара')
	name_category = models.CharField(max_length=100)
	category_description = models.TextField(max_length=1000, help_text='Описание категории товара')

	def __str__(self):
		return self.category_description
		# return f'{self.id_category} {self.name_category} {self.category_description}'
		# return self.name_category, self.category_description
		# return list(self.name_category), list(self.category_description)

	def get_absolute_url(self):
		return reverse('index')



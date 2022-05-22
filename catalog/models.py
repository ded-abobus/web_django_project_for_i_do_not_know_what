
#не изменил (id product)

from django.db import models
from django.urls import reverse
import uuid

class ProductModel(models.Model):
	#id_product = models.UUIDField(primary_key=True, default=lambda: str(uuid.uuid4()), help_text='Уникальный идентификатор товара')
	id_product = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text='Уникальный идентификатор товара')
	#if isinstance(hex, uuid.UUID): hex, int = None, hex.int
	category = models.ForeignKey('CategoryModel', on_delete=models.SET_NULL, null=True) #id_category
	name_product = models.CharField(max_length=100)
	description = models.TextField(max_length=1000, help_text='Краткое описание товара')
	long_description = models.TextField(max_length=1500, help_text='Длинное описание товара')

#	def process_result_value(self, id_product, dialect):
#		if value is None:
#			return value
#		else:
#			return uuid.UUID(str(value))

	def __str__(self):
                #return self.id_product
		return f'{self.name_product} ({self.category.name_category})'

	def get_absolute_url(self):
		return reverse('index')

class CategoryModel(models.Model):
	id_category = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text='Уникальный идентификатор категории товара')
	#if isinstance(hex, uuid.UUID): hex, int = None, hex.int
	#id_category = models.UUIDField(as_uuid=True, primary_key=True, default=uuid.uuid4, help_text='Уникальный идентификатор категории товара')
	name_category = models.CharField(max_length=100)
	category_description = models.TextField(max_length=1000, help_text='Описание категории товара')

	def __str__(self):
		return self.name_category

	def get_absolute_url(self):
		return reverse('index')



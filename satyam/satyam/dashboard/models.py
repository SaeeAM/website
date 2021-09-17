from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

# Create your models here.

class Service(models.Model):
	Department = [
		('default', 'Choose Option'),
		('digital', 'Digital Service'),
		('govtscheme', 'Govt Service'),
		('student', 'Student Service'),
		('common', 'Common Service'),
		('business', 'Business Service'),
		('notification', 'Notification Service'),
		('other', 'Other Service'),
	]
	category = models.CharField(max_length=80, choices=Department, default='default')
	name = models.CharField(max_length=200, unique=True)
	discription = RichTextField()

	class Meta:
		verbose_name = "service"
		verbose_name_plural = "service"
		ordering = ['category']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
    		return reverse('detail', kwargs={'pk': self.pk})

class Document(models.Model):
	service_name= models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)
	document= RichTextField()

	class Meta:
	   verbose_name = "document"
	   verbose_name_plural = "document"
	   ordering = ['document']

	def __str__(self):
		return self.document



class Costumer(models.Model):
	name = models.CharField(max_length=200)
	phone = PhoneNumberField()
	email = models.CharField(max_length=200)
	message = models.TextField(max_length=200, blank=True)
	choose_service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)
	service_document = models.ForeignKey(Document, on_delete=models.SET_NULL, blank=True, null=True)
	document = models.FileField(upload_to='service/document/')
	date_uploaded = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return f'{self.name} {self.phone} {self.email}'


class Track(models.Model):
	trackid= models.IntegerField(primary_key=True)
	name= models.ForeignKey(Costumer, on_delete=models.SET_NULL, blank=True, null=True)
	link= models.URLField(default="")
	comp_time= models.DateTimeField(auto_now_add=True, )
	message= models.TextField()

	class Meta:
	   verbose_name = "track"
	   verbose_name_plural = "Track"
	   ordering = ['comp_time']

	def __int__(self):
		return self.pk
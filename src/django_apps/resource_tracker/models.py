from django.db import models

class Resource(models.Model):
	name = models.CharField('Resource Name', max_length=200)
	unit = models.CharField('Measurement Unit', max_length=200)
	curr_amt = models.CharField('Current Amount', max_length=200)
	current_date_time = models.DateTimeField('Current Date and Time')
	def __unicode__(self):
		return self.name

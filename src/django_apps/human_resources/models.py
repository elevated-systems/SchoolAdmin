from django.db import models

GENDER_CHOICES = (
	(u'M', u'Male'),
	(u'F', u'Female'),
	)

class Teacher(models.Model):
	first_name = models.CharField('First Name', max_length=200)
	last_name = models.CharField('Last Name', max_length=200)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
	def __unicode__(self):
		return self.last_name + ', ' + self.first_name

from django.db import models
import datetime

year = datetime.timedelta(365)
num_mon_year = 12
num_day_mon = 30
GENDER_CHOICES = (
	(u'M', u'Male'),
	(u'F', u'Female'),
	)

class Location(models.Model):
	name = models.CharField('Location Name', max_length=200)
	street_addr_ln1 = models.CharField('Address Line 1', max_length=200)
	street_addr_ln2 = models.CharField('Address Line 2 (optional)', blank=True, max_length=200)
	city = models.CharField('City', max_length=200)
	state = models.CharField('State', max_length=2)
	max_enrollment = models.IntegerField('Max Enrollment')
	enrollment = models.IntegerField('Actual Enrollment')
	def __unicode__(self):
		return self.name

class Student(models.Model):
	first_name = models.CharField('First Name', max_length=200)
	last_name = models.CharField('Last Name', max_length=200)
	d_o_b = models.DateField('Date of Birth')
	#gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
	father_first_name = models.CharField('Father - First Name', blank=True, max_length=200)
	father_last_name = models.CharField('Father - Last Name', blank=True, max_length=200)
	father_email_addr = models.EmailField('Father - Email Address', blank=True)
	mother_first_name = models.CharField('Mother - First Name', blank=True, max_length=200)
	mother_last_name = models.CharField('Mother - Last Name', blank=True, max_length=200)
	mother_email_addr = models.EmailField('Mother - Email Address', blank=True)
	family_street_addr_ln1 = models.CharField('Address Line 1', max_length=200)
	family_street_addr_ln2 = models.CharField('Address Line 2 (optional)', blank=True, max_length=200)
	family_city = models.CharField('City', max_length=200)
	family_state = models.CharField('State', max_length=2)
	location = models.ForeignKey(Location)
	
	def __unicode__(self):
		return self.last_name + ', ' + self.first_name
	
	def age_years(self):
		return (datetime.date.today() - self.d_o_b).days / year.days
	age_years.short_description = 'Years'
	
	def age_months(self):
		return (((datetime.date.today() - self.d_o_b).days) % year.days) / num_day_mon
	age_months.short_description = 'Months'
	
	def age_total_months(self):
		return (self.age_years() * num_mon_year) + self.age_months()
	age_total_months.short_description = 'Age entirely in Months'
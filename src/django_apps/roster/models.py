from google.appengine.ext import db
import datetime

year = datetime.timedelta(365)
num_mon_year = 12
num_day_mon = 30

class Location(db.Model):
	name = db.StringProperty('Location Name', required=True)
	street_addr = db.PostalAddressProperty('Address', required=True)
	city = db.StringProperty('City', required=True)
	state = db.StringProperty('State', required=True)
	max_enrollment = db.IntegerProperty('Max Enrollment', required=True)
	enrollment = db.IntegerProperty('Actual Enrollment')
	def __unicode__(self):
		return self.name

class Student(db.Model):
	first_name = db.StringProperty('First Name', required=True)
	last_name = db.StringProperty('Last Name', required=True)
	d_o_b = db.DateProperty('Date of Birth', required=True)
	gender = db.StringProperty('Gender', required=True, choices=set(["Male", "Female"]))
	father_first_name = db.StringProperty('Father - First Name')
	father_last_name = db.StringProperty('Father - Last Name')
	father_email_addr = db.EmailProperty('Father - Email Address')
	mother_first_name = db.StringProperty('Mother - First Name')
	mother_last_name = db.StringProperty('Mother - Last Name')
	mother_email_addr = db.EmailProperty('Mother - Email Address')
	family_street_addr = db.PostalAddressProperty('Address', required=True)
	family_city = db.StringProperty('City', required=True)
	family_state = db.StringProperty('State', required=True)
	location = db.ReferenceProperty(Location)
	
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
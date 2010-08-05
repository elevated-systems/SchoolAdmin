from roster.models import Location, Student
from django.contrib import admin

class StudentAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'age_years', 'age_months', 'age_total_months')
	search_fields = ['last_name', 'first_name']

admin.site.register(Student, StudentAdmin)
admin.site.register(Location)
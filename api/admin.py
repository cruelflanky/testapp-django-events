from django.contrib import admin

from .models import *
# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Event._meta.fields]

	class Meta:
		model = Event

admin.site.register(Event, EventAdmin)

class CityAdmin(admin.ModelAdmin):
	list_display = [field.name for field in City._meta.fields]

	class Meta:
		model = City

admin.site.register(City, CityAdmin)
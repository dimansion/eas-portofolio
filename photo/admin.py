from django.contrib import admin
from .models import Work

class WorkAdmin(admin.ModelAdmin):
	list_display = ["name", "category"]
	list_filter = ["category"]

	class Meta:
		model = Work

admin.site.register(Work, WorkAdmin)

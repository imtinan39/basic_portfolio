from django.contrib import admin

# Register your models here.


class InfoAdmin(admin.ModelAdmin):
	readonly_fields=('created',)
from .models import Info,Pickle

admin.site.register(Info,InfoAdmin)
admin.site.register(Pickle)
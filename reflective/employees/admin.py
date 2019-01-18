from django.contrib import admin
from .models import Employee, Department, EffectiveDate

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(EffectiveDate)

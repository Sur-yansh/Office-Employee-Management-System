from django.contrib import admin
from .models import Role, Department, Employee

# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)

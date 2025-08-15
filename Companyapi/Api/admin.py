from django.contrib import admin
from Api.models import Company, Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name', 'location', 'types')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'company')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
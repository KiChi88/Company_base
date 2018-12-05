from django.contrib import admin
from . models import Employee, Department

class EmployeeData(admin.ModelAdmin):
    list_display = ['full_name', 'department']
    list_filter = ['department']
    search_fields = [
        'first_name', 'last_name', 'middle_name', 'borth_date', 'email', 'phone', 'data_start', 'data_end', 'role'
    ]
    class Meta:
        model = Employee

admin.site.register(Employee, EmployeeData)
admin.site.register(Department)

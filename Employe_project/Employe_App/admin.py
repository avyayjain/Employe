from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Employee,Position
# Register your models here.

#admin.site.register(Employee)

@admin.register(Employee)
class Employee_Admin(admin.ModelAdmin):
    list_display = ['emp_id','emp_name','emp_mobile_no','emp_email','emp_address','emp_dob']

@admin.register(Position)
class Emp_postion(admin.ModelAdmin):
      display = ['postion']  
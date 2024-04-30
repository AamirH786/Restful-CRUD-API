from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'fname','lname', 'email', 'salary','department', 'status')
    search_fields = ('fname', 'email','department',)
    list_filter = ('status',)

from django.contrib import admin

from Insurance.models import Insurance
from Insurance.models import UnderWriter
from Insurance.models import Branch
from Insurance.models import Employee

from Insurance.models import Insurance_Policy
from Insurance.models import Insurance_Discount
from Insurance.models import Customer

# Register your models here.

class CustomerList(admin.ModelAdmin):
	list_discount = ('Customer_First_Name'+'Customer_Last_Name'+'Customer_Middle_Name')

class DiscountList(admin.ModelAdmin):
	list_discount = ('Discount_Title','Discount_Description')


class PageAdmin(admin.ModelAdmin):
	list_display = ('Branch_Address', 'Employee_Full_Name')

class InsurancePolicy(admin.ModelAdmin):
	list_display = ('Policy_Name','Insurance_Title')

class InsuranceList(admin.ModelAdmin):
	list_display = ('Insurance_Title','Publication_Date','Publication_End','UnderWriter_Name')

class UnderWriterList(admin.ModelAdmin):
	list_display = ('UnderWriter_Company_Name','UnderWriter_Email','UnderWriter_Contact_Number')

class EmployeeList(admin.ModelAdmin):
	list_display = ('Employee_Full_Name','Employee_Email','Employee_Position')

admin.site.register(Customer,CustomerList)
admin.site.register(Employee,EmployeeList)
admin.site.register(UnderWriter,UnderWriterList)
admin.site.register(Insurance,InsuranceList)
admin.site.register(Insurance_Policy,InsurancePolicy)
admin.site.register(Branch, PageAdmin)
admin.site.register(Insurance_Discount,DiscountList)
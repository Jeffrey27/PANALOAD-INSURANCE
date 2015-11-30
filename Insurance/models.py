from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class UnderWriter(models.Model):
	UnderWriter_Company_Name = models.CharField(max_length = 200,default='', verbose_name='Company Name')
	UnderWriter_Contact_Number = models.PositiveIntegerField(default='09',verbose_name='Contact Number',validators=[MaxValueValidator(99999999999)])
	Account_Username = models.CharField(max_length = 200,default='',verbose_name='Account Username')
	Account_Password = models.CharField(max_length = 200,default='',verbose_name='Account Password')
	UnderWriter_Email = models.CharField(max_length = 200, default='', verbose_name='Company Email')
	UnderWriter_Main_Office_Address = models.CharField(max_length =200, default='',verbose_name='Main Office')
	Contract_Expiration = models.DateTimeField(default =datetime.datetime.now,verbose_name = 'Contract Expiration Date',editable=True)


	def __str__(self):
		return self.UnderWriter_Company_Name

	class Meta:
		verbose_name="UnderWriter"



class Insurance(models.Model):
	Insurance_Title = models.CharField(max_length = 200, default ='', verbose_name = 'Insurance Title')
	Insurance_Description = models.TextField(max_length=500,default='',verbose_name = 'Insurance Description')
	Insurance_Selling_Price = models.DecimalField(validators=[MinValueValidator(0)],max_digits=30,decimal_places=2,default =0,verbose_name = 'Insurance Selling Price')
	Insurance_Base_Price = models.DecimalField(max_digits=30,validators=[MinValueValidator(0)],decimal_places=2,default =0,verbose_name = 'Insurance Base Price')
	Publication_Date = models.DateTimeField(default =datetime.datetime.now,verbose_name = 'Publication Date',editable=True)
	Publication_End = models.DateTimeField(default= datetime.datetime.now, verbose_name = 'Date End',editable=True)
	Insurance_Benefits = models.TextField(default='',max_length=500,verbose_name='Insurance Benefit')
	UnderWriter_Name = models.ForeignKey('UnderWriter', verbose_name = 'UnderWriter Company')

	def __str__(self):
		return self.Insurance_Title

	class Meta:
		verbose_name="Insurance"


class Insurance_Policy(models.Model):
	Policy_Name = models.TextField(max_length=500, default='', verbose_name = 'Insurance Policy')
	Insurance_Title = models.ForeignKey('Insurance',verbose_name='Insurance Title')

	def __str__(self):
		return self.Policy_Name

	class Meta:
		verbose_name="Insurance Policy"


class Insurance_Discount(models.Model):
	Discount_Title = models.CharField(max_length=500, default='', verbose_name = 'Discount Title')
	Discount_Description = models.TextField(max_length=500,default='',verbose_name = 'Discount Description')
	Discount_Percent = models.DecimalField(max_digits=30,decimal_places=2,default =0,verbose_name = 'Discount Percent')

	def __str__(self):
		return self.Discount_Title

	class Meta:
		verbose_name="Discount for Insurance"

class Employee(models.Model):
	Employee_Full_Name = models.CharField(max_length=200, blank=False, default='',verbose_name ='Employee Full Name')
	Employee_Email = models.CharField(max_length=200, blank=False, default='', verbose_name='Email')
	Employee_Contact_Number = models.PositiveIntegerField(default='09',verbose_name='Contact Number',validators=[MaxValueValidator(99999999999)])
	Employee_Position = models.CharField(max_length=200, blank=False, default='',verbose_name='Applied Position')
	Employee_Username = models.CharField(max_length=200, blank=False, default='',verbose_name='Account Username')
	Employee_Password = models.CharField(max_length=200, blank=False, default='',verbose_name ='Account Password')
	
	def __str__(self):
		return self.Employee_Full_Name

	class Meta:
		verbose_name ="Employee"

class Branch(models.Model):
	Branch_Address = models.CharField(max_length = 200, default='', verbose_name= 'Branch Address')
	Branch_Contact_Number = models.PositiveIntegerField(default='09',verbose_name='Contact Number',validators=[MaxValueValidator(99999999999)])
	Employee_Full_Name = models.ForeignKey('Employee',verbose_name='Employee in charge')
	

	def __str__(self):
		return self.Branch_Address

	class Meta:
		verbose_name = 'Branche'

class Customer(models.Model):
	Customer_Full_Name = models.CharField(max_length = 200, default='', verbose_name= 'Full Name')
	Customer_Contact_Number = models.PositiveIntegerField(default='09',verbose_name='Contact Number',validators=[MaxValueValidator(99999999999)])
	Customer_Age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(150)], default='00',verbose_name='Age')
	Customer_Address = models.CharField(max_length = 200, default='', verbose_name= 'Address')
	Insurance_Title = models.ForeignKey('Insurance',verbose_name='Insurance Preferred')
	Apply_Date = models.DateTimeField(default =datetime.datetime.now,verbose_name = 'Application Date',editable=True)

	def __str__(self):
		return self.Customer_Full_Name

	class Meta:
		verbose_name = 'Customer'

	
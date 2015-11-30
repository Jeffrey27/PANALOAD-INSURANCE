# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Branch_Address', models.CharField(max_length=200, default='', verbose_name='Branch Address')),
                ('Branch_Contact_Number', models.PositiveIntegerField(default='09', validators=[django.core.validators.MaxValueValidator(99999999999)], verbose_name='Contact Number')),
            ],
            options={
                'verbose_name': 'Branche',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Customer_Full_Name', models.CharField(max_length=200, default='', verbose_name='Full Name')),
                ('Customer_Contact_Number', models.PositiveIntegerField(default='09', validators=[django.core.validators.MaxValueValidator(99999999999)], verbose_name='Contact Number')),
                ('Customer_Age', models.IntegerField(default='00', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)], verbose_name='Age')),
                ('Customer_Address', models.CharField(max_length=200, default='', verbose_name='Address')),
                ('Apply_Date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Application Date')),
            ],
            options={
                'verbose_name': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Employee_Full_Name', models.CharField(max_length=200, default='', verbose_name='Employee Full Name')),
                ('Employee_Email', models.CharField(max_length=200, default='', verbose_name='Email')),
                ('Employee_Contact_Number', models.PositiveIntegerField(default='09', validators=[django.core.validators.MaxValueValidator(99999999999)], verbose_name='Contact Number')),
                ('Employee_Position', models.CharField(max_length=200, default='', verbose_name='Applied Position')),
                ('Employee_Username', models.CharField(max_length=200, default='', verbose_name='Account Username')),
                ('Employee_Password', models.CharField(max_length=200, default='', verbose_name='Account Password')),
            ],
            options={
                'verbose_name': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Insurance_Title', models.CharField(max_length=200, default='', verbose_name='Insurance Title')),
                ('Insurance_Description', models.TextField(max_length=500, default='', verbose_name='Insurance Description')),
                ('Insurance_Selling_Price', models.DecimalField(default=0, max_digits=30, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Insurance Selling Price')),
                ('Insurance_Base_Price', models.DecimalField(default=0, max_digits=30, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Insurance Base Price')),
                ('Publication_Date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Publication Date')),
                ('Publication_End', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date End')),
                ('Insurance_Benefits', models.TextField(max_length=500, default='', verbose_name='Insurance Benefit')),
            ],
            options={
                'verbose_name': 'Insurance',
            },
        ),
        migrations.CreateModel(
            name='Insurance_Discount',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Discount_Title', models.CharField(max_length=500, default='', verbose_name='Discount Title')),
                ('Discount_Description', models.TextField(max_length=500, default='', verbose_name='Discount Description')),
                ('Discount_Percent', models.DecimalField(default=0, max_digits=30, decimal_places=2, verbose_name='Discount Percent')),
            ],
            options={
                'verbose_name': 'Discount for Insurance',
            },
        ),
        migrations.CreateModel(
            name='Insurance_Policy',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Policy_Name', models.TextField(max_length=500, default='', verbose_name='Insurance Policy')),
                ('Insurance_Title', models.ForeignKey(to='Insurance.Insurance', verbose_name='Insurance Title')),
            ],
            options={
                'verbose_name': 'Insurance Policy',
            },
        ),
        migrations.CreateModel(
            name='UnderWriter',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('UnderWriter_Company_Name', models.CharField(max_length=200, default='', verbose_name='Company Name')),
                ('UnderWriter_Contact_Number', models.PositiveIntegerField(default='09', validators=[django.core.validators.MaxValueValidator(99999999999)], verbose_name='Contact Number')),
                ('Account_Username', models.CharField(max_length=200, default='', verbose_name='Account Username')),
                ('Account_Password', models.CharField(max_length=200, default='', verbose_name='Account Password')),
                ('UnderWriter_Email', models.CharField(max_length=200, default='', verbose_name='Company Email')),
                ('UnderWriter_Main_Office_Address', models.CharField(max_length=200, default='', verbose_name='Main Office')),
                ('Contract_Expiration', models.DateTimeField(default=datetime.datetime.now, verbose_name='Contract Expiration Date')),
            ],
            options={
                'verbose_name': 'UnderWriter',
            },
        ),
        migrations.AddField(
            model_name='insurance',
            name='UnderWriter_Name',
            field=models.ForeignKey(to='Insurance.UnderWriter', verbose_name='UnderWriter Company'),
        ),
        migrations.AddField(
            model_name='customer',
            name='Insurance_Title',
            field=models.ForeignKey(to='Insurance.Insurance', verbose_name='Insurance Preferred'),
        ),
        migrations.AddField(
            model_name='branch',
            name='Employee_Full_Name',
            field=models.ForeignKey(to='Insurance.Employee', verbose_name='Employee in charge'),
        ),
    ]

from django.test import TestCase
from selenium import webdriver
from django.test import LiveServerTestCase
# Create your tests here.
from django.test import TestCase
from django.utils import timezone
from Insurance.models import Insurance
from Insurance.models import UnderWriter
#from Insurance.models import UnderWriter
import sys

class InsuranceModelTest(LiveServerTestCase):
	#def test_creating_a_new_underwriter(self):
	#	underwriter= UnderWriter()
	#	underwritername="Pro-life"

	#	underwriter.save()

	#	all_underwriter_in_database = UnderWriter.objects.all()
	#	self.assertEquals(len(all_underwriter_in_database),1)
	##	only_underwriter_in_database = all_underwriter_in_database[0]
	#	self.assertEquals(only_underwriter_in_database,underwriter)

	#	self.assertEquals(only_underwriter_in_database.UnderWriter_Name,"Pro-life")

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) 
    
    def tearDown(self):
        self.browser.quit() 

    def test_can_log_in_admin(self):
        #admin page
        self.browser.get(self.live_server_url + '/admin/')

        #Django administration heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('PANALOAD INSURANCE', body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)

    def test_creating_a_new_insurance_and_saving_it_to_the_database(self):

        # start by creating a new Poll object with its "question" set
        underwriter = UnderWriter()
        UnderWriter_Company_Name = "What's up?"
        UnderWriter_Contact_Number = 12

        # check we can save it to the database
        underwriter.save()

        # now check we can find it in the database again
        all_insurance_in_database = Insurance.objects.all()
        self.assertEquals(len(all_insurance_in_database), 1)
        only_insurance_in_database = all_insurance_in_database[0]
        self.assertEquals(only_insurance_in_database, underwriter)

        # and check that it's saved its two attributes: question and pub_date
        self.assertEquals(only_insurance_in_database.UnderWriter_Name, "What's up?")
        self.assertEquals(only_insurance_in_database.pub_date, underwriter.UnderWriter_Contact_Number)


#    UnderWriter_Company_Name = models.CharField(max_length = 200,default='', verbose_name='Company Name')
#   UnderWriter_Contact_Number = models.IntegerField(max_length=11, default='09',verbose_name='Contact Number')
#    Account_Username = models.CharField(max_length = 200,default='',verbose_name='Account Username')
#    Account_Password = models.CharField(max_length = 200,default='',verbose_name='Account Password')
#    UnderWriter_Email = models.CharField(max_length = 200, default='', verbose_name='Company Email')
#    UnderWriter_Main_Office_Address = models.CharField(max_length =200, default='',verbose_name='Main Office')
#    Contract_Expiration = models.DateTimeField(default =datetime.datetime.now,verbose_name = 'Contract Expiration Date',editable=True)




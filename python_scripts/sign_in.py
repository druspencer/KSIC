#sign in class
#is called by test.py as an object
#signs into an account with given credentials

from selenium import webdriver #for selenium 
from selenium.webdriver.common.keys import Keys #for keypresses
import os, sys #for writing to directory
import time #for executing waits
import slow #extra module written to take a string, text field and a text speed

class Sign_in_out():
	
	def setUp(self, target, email, browser): #set up method takes in target site, email address and browser
		#statements to select correct browser
		if browser == "firefox":
			self.driver = webdriver.Firefox()
		if browser == "chrome":
			self.driver = webdriver.Chrome()
		if browser == "IE":
			self.driver = webdriver.Ie()
		self.email_address = email #pulling given email address into a local variable
		self.password = "qwerty" #default pw for all new accounts
		self.target = target #pulling given site into a local variable
		self.browser = browser #pulling given browser into a local variable
				
	def test_sign_in_out(self, path): #actual testing method takes in directory for iteration
		driver = self.driver
		driver.get("http://"+self.target) #opens given browser on given target
		driver.maximize_window() #maximises driver window
		target_path = path+'/'+self.target+'/'+self.browser+self.email_address #sets path and name for screenshot
		driver.save_screenshot(target_path+'_sign_in_on_load.png') #saves screenshot
		sign_in = driver.find_element_by_link_text("Sign in") #finds and clicks the sign in link
		sign_in.click()
		
		time.sleep(2) #pauses
		driver.switch_to_alert() #switches to modal
		
		#finds username and pw fields on the modal
		email_input = driver.find_element_by_name("loginID")
		password_input = driver.find_element_by_id("sign-in-password")
		
		time.sleep(2) #pauses
		#calls the only method of the type_slow object to input data into above found fields 
		slow.type_slow(self, self.email_address, email_input, 1)
		slow.type_slow(self, self.password, password_input, 1)
		
		driver.save_screenshot(target_path+'_sign_in_form.png') #saves screenshot
		time.sleep(2) #pauses
		sign_in_button = driver.find_element_by_xpath("//input[@value='Sign in']") #it finds and clicks the modal's sign in button
		sign_in_button.click()
		
		time.sleep(2) #pauses
		driver.save_screenshot(target_path+'_after_sign_in.png') #saves screenshot
		sign_out = driver.find_element_by_link_text("Sign out") #finds and clicks the sign out button
		sign_out.click()
		
		time.sleep(2) #pauses
		
	def tearDown(self): #method which is called by test.py to kill instance
		self.driver.close()
		
		
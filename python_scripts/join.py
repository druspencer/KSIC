#join class
#is called by test.py as an object
#creates a new account with the email address passed in


from selenium import webdriver #for selenium 
from selenium.webdriver.common.keys import Keys #for keypresses
from selenium.common.exceptions import NoSuchElementException #for error handling (test verification in future)
import os, sys #for writing to directory
import datetime #for a detailed timestamp on email
import time #for executing waits
import slow #extra module written to take a string, text field and a text speed

class Join():

	def get_email(self): #method to create unique email address
		time_stamp = datetime.datetime.now() #grab timestamp for unique email address
		email = "LG_"+time_stamp.strftime('%Y%m%d%H%M%S')+"@stv2.tv" #creates email address
		return email
	
	def setUp(self, target, email, browser): #set up method takes in target site, email address and browser
		#statements to select correct browser
		if browser == "firefox":
			self.driver = webdriver.Firefox()
		if browser == "chrome":
			self.driver = webdriver.Chrome()
		if browser == "IE":
			self.driver = webdriver.Ie()
		self.password = "qwerty" #default pw for all new accounts
		self.email_address = email #pulling given email address into a local variable
		self.target = target #pulling given site into a local variable
		self.browser = browser #pulling given browser into a local variable
		
	def test_join(self, path): #actual testing method takes in directory for iteration
		typespeed = 1 #modifier for typing speed, used later
		driver = self.driver
		driver.get("http://"+self.target) #opens given browser on given target
		driver.maximize_window() #maximises driver window
		target_path = path+'/'+self.target #sets path to a sub folder in the directory
		if not os.path.exists(target_path):
			os.makedirs(target_path) # creates sub folder
		target_path = path+'/'+self.target+'/'+self.browser+self.email_address #sets path and name for screenshot
		driver.save_screenshot(target_path+'_join_on_load.png') #saves screenshot
		join = driver.find_element_by_link_text("Join") #finds join button on site
		join.click() #clicks join button on site
		
		time.sleep(2) #waits 2s
		driver.switch_to_alert() #switches to modal
		
		#finds various input fields in join modal
		firstname_input = driver.find_element_by_name("firstName") 
		lastname_input = driver.find_element_by_name("lastName")
		email_input = driver.find_element_by_id("email")
		password_input = driver.find_element_by_id("registration-password")
		password_retype_input = driver.find_element_by_id("passwordRetype")
		dob_input = driver.find_element_by_id("dob")
		postcode_input = driver.find_element_by_id("address")
		
		#calls the only method of the type_slow object to input data into above found fields 
		slow.type_slow(self, "test", firstname_input, 1) #firstname is test
		slow.type_slow(self, "test", lastname_input, 1) #surname is test
		slow.type_slow(self, self.email_address, email_input, 1) #email address has been carried in
		slow.type_slow(self, self.password, password_input, 1) #password has been carried in
		slow.type_slow(self, self.password, password_retype_input, 1) #password retype
		slow.type_slow(self, "18061991", dob_input, 1) #dob is 18/06/1991
		
		#loop to deal with particularly nasty javascript address picker which searches addresses while the user types postcode
		#often flakes out and does not display address despite having correct postcode
		#this loop will repeat until it sees the expected address, types slower each time
		while True:
			postcode_input.clear() #clears input field at the start of each loop
			time.sleep(0.5) #pauses
			slow.type_slow(self, "ENTER POSTCODE HERE ", postcode_input, typespeed) #types postcode slowly
			try: #if it sees the correct address then click it and break the loop
				driver.find_element_by_xpath("//*[contains(text(), 'ENTER EXPECTED ADDRESS HERE')]").click()
				break
			except NoSuchElementException: #if it does not see the address this exception will be thrown by selenium which can be caught and handled
				print "Address not found yet" #print feedback
				typespeed = typespeed * 1.1 #type slower next time
		
		driver.save_screenshot(target_path+'_join_form.png') #takes a screenie
		time.sleep(2) #pauses
		sign_in_button = driver.find_element_by_xpath("//input[@value='Join now']") #finally it finds and clicks the confirmation button
		sign_in_button.click() 
		
		time.sleep(5) #pauses
		driver.save_screenshot(target_path+'_after_join.png') #takes a screenie
		sign_out = driver.find_element_by_link_text("Sign out") #finds and clicks sign out link after joining 
		sign_out.click() 
		
	def tearDown(self): #method which is called by test.py to kill instance
		self.driver.close() 

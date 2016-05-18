import time, datetime #for waits
from selenium import webdriver #for web elements
from selenium.webdriver.common.keys import Keys #for keypresses

def type_slow(word, input, factor): #takes in string, input field and speed factor
	for l in word: #runs a loop for how long the string is
		input.send_keys(l) #inputs the string character by character
		time.sleep(0.05*factor) #waits between entries
		
def gen_email():
	email = "LG_"+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"@stv2.tv"
	return email
	
def log(message):
	log = "["+datetime.datetime.now().strftime('%H:%M:%S')+"] "+message
	print log
	
<<<<<<< HEAD
def sign_in(emailaddress, password, handler, driver):
	#TODO add code to sign in
	
	try:element = driver.find_element_by_link_text("Sign in/Join")
	except:element = None #ignore the exception, will be thrown again and handled in the testHandler class		
	handler.elementClick(
	element, 
	"Click the Sign In button", 
	"Link is clickable")
	
	time.sleep(0.5)
	
	try:element = driver.find_element_by_class_name("")
	except:element = None #ignore the exception, will be thrown again and handled in the testHandler class	
	handler.assertText(
	element,
	"Check 'Enter Email Address' modal is displayed",
	"")
	
	time.sleep(0.5)
	
	try:element = driver.find_element_by_id("emailFormEmail")
	except:element = None #ignore the exception, will be thrown again and handled in the testHandler class	
	handler.elementInput(
	element,
	emailaddress,
	"Enter email address into input field",
	"Email address appears in field")
	
	time.sleep(0.5)
	
	try:element = driver.find_element_by_xpath("//input[@value='Continue']")
	except:element = None #ignore the exception, will be thrown again and handled in the testHandler class		
	handler.elementClick(
	element, 
	"Click the Continue button", 
	"Button is clickable")
	
	time.sleep(0.5)
	
	try:element = driver.find_elements_by_class_name("")[1]
	except:element = None #ignore the exception, will be thrown again and handled in the testHandler class		
	handler.assertValue(
	element,
	"Check Welcome Back Modal is displayed", 
	"Sign In")
	
	time.sleep(0.5)
	
	try:element = driver.find_element_by_id("signInFormPassword")
	except:element = None #ignore the exception, will be thrown again and handled in the testHandler class		
	handler.elementInput(
	element,
	password,
	"Enter password into input field",
	"Password address appears in field")
	
	time.sleep(0.5)
	
	try:element = driver.find_elements_by_class_name("")[1]
	except:element = None #ignore the exception, will be thrown again and handled in the testHandler class		
	handler.elementClick(
	element,
	"Click the Sign In button",
	"Button is clickable")
	
	time.sleep(0.5)
	
	try:element = driver.find_element_by_id("registration---sign-out-nav")
	except:element = None #ignore the exception, will be thrown again and handled in the testHandler class	
	handler.assertText(
	element,
	"Check Sign In was successful",
	"Sign out")
	
def join(email):
=======
def sign_in():
	#TODO add code to sign in
	print "sign in"
	
def join():
>>>>>>> 5d88b0e5b0ac3f42feb4360411c27eed4680bd96
	#TODO add code to join/create an account
	print "join"
	
	
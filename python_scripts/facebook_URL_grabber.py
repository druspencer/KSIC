from selenium import webdriver

#instantiates some variables we use later 
clear = "\n" * 100
confirmation1 = ""
confirmation2 = ""
browser = ""

#defines two methods: 
#login fills in the given credentials into the FB homepage
#getUserID can be called on a users page to grab and slice the URL to get the users ID
def login(email_address, password):	
	email_input.send_keys("%s" % (email_address))
	password_input.send_keys("%s" % (password))
	login_button.click()
def getUserID(url):	
	urlList = url.split("https://www.facebook.com/")
	return urlList[1]
	
#this is where we start talking to the user
print clear
print "================================================================"
print ""
print "Hello!"
print ""
print "Welcome to Facebook Personal URL finder 3000 TM"
print ""
#three while loops for input validation of email address, password and browser choice
while confirmation1 != "Y" or confirmation1 != "y":
	email_address = raw_input("Please provide your Facebook email address: ")
	print ""
	print "You've provided: %s is that correct? Y for Yes or N for No"% (email_address)
	confirmation1 = raw_input()
	print ""
while confirmation2 != "Y" or confirmation2 != "y":
	password = raw_input("Please provide your Facebook password: ")
	print ""
	print "You've provided: %s is that correct? Y for Yes or N for No" % (password)
	confirmation2 = raw_input()
	print ""
while browser != "Chrome" and browser != "chrome" and browser != "Firefox" and browser != "firefox":
	browser = raw_input("Would you prefer Chrome or Firefox? ")
	if browser == "Chrome" or browser == "chrome":
		print "Please wait... Launching Chrome..."
		driver = webdriver.Chrome()
	if browser == "Firefox" or browser == "firefox":
		print "Please wait... Launching Firefox..."
		driver = webdriver.Firefox()

driver.get("http://www.facebook.com")
#finds the credential elements by their IDs
email_input = driver.find_element_by_id("email")
password_input = driver.find_element_by_id("pass")
login_button = driver.find_element_by_id("loginbutton")
#calls the login method
login(email_address,password)
#navigates to users page
visit_profile = driver.find_element_by_class_name("fbxWelcomeBoxName")
visit_profile.click()
#here we spit out the users ID by calling the above method
print ""
print "Your Facebook URL extension is: %s" %(getUserID(driver.current_url))
print ""
print "Thanks for using Facebook Personal URL finder 3000 TM"
print ""
print "================================================================"
driver.quit()
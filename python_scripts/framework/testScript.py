import testHandler, datetime, time,testCollections #for writing to directories - only used for screenies just now
from selenium import webdriver #for web elements

#this is where the magic happens
#user should only need to edit this file
#currently configured only to open and close a modal
#any reference to actual sites have been removed

try:
	clear = "\n" * 100
	print clear
	time_stamp = datetime.datetime.now() #initialises time object 
	execution_time = time_stamp.strftime('%d_%m_%Y %H%M')  #grab time for various timestamps
	path = 'C:/Selenium_Reports/'+execution_time #sets directory for this execution

	handler = testHandler.testHandler(path)
	driver = webdriver.Chrome() 
	driver.get("")#target here
	driver.maximize_window()
	driver.implicitly_wait(2)

	testCollections.sign_in("", "", handler, driver)
	

except KeyboardInterrupt:
	print "KeyboardInterrupt"
	
finally:
	handler.endTesting(driver)
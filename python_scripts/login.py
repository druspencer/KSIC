from selenium import webdriver
from sys import argv

script, page_url, email_address, password = argv

print ("Opening %s" % (page_url))
print ("Email Address: %s" % (email_address))
print ("Password: %s" % (password))

driver = webdriver.Firefox()
driver.get("http://www.%s" % (page_url)) 

email_input = driver.find_element_by_id("email")
password_input = driver.find_element_by_id("pass")
login_button = driver.find_element_by_id("loginbutton")

email_input.send_keys("%s" % (email_address))
password_input.send_keys("%s" % (password))
login_button.click()

print "Complete"

driver.quit ()


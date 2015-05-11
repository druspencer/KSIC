from selenium import webdriver
import getpass

page_url = raw_input("Website (e.g. facebook.com): ")
email_address = raw_input("Email: ")
password = getpass.getpass("Password: ")

print "Launching Firefox"

driver = webdriver.Firefox()
driver.get("http://www.%s" % (page_url)) 

email_input = driver.find_element_by_id("email")
password_input = driver.find_element_by_id("pass")
login_button = driver.find_element_by_id("loginbutton")



email_input.send_keys("%s" % (email_address))
password_input.send_keys("%s" % (password))
login_button.click()

print "Complete"

driver.quit()

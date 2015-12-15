from selenium import webdriver
import getpass
import time

user_name = raw_input("User Name:")
password = getpass.getpass("Password: ")

print "Launching Firefox"

driver = webdriver.Firefox()
driver.get("https://web.skype.com/en/") 
time.sleep(15)
email_input = driver.find_element_by_id("username")
password_input = driver.find_element_by_id("password")
login_button = driver.find_element_by_id("signIn")


print "Sending keys - name"
email_input.send_keys("%s" % (user_name))
print "Sending keys - pass"
password_input.send_keys("%s" % (password))
print "Connecting"
login_button.click()

print "Complete"
time.sleep(15)
print "Entering Message"
message_input = driver.find_element_by_name("messageInput")
message_input.send_keys("Dru Bot says hello world - I am automated")
print "Sent"
send_button = driver.find_element_by_css_selector("button.btn.circle.send-button.large[type='Button']")
send_button.click()

#driver.quit()

from Tkinter import *
import ttk
from selenium import webdriver

#Here we define four methods for a few different things

#chrome() does the whole execution in chrome
def chrome():
	driver = webdriver.Chrome()
	driver.get("http://www.facebook.com")
	email_input = driver.find_element_by_id("email")
	password_input = driver.find_element_by_id("pass")
	login_button = driver.find_element_by_id("loginbutton")
	login(email.get(),password.get(), email_input, password_input, login_button)
	visit_profile = driver.find_element_by_class_name("fbxWelcomeBoxName")
	visit_profile.click()
	ID.set(getUserID(driver.current_url))
#firefox() does the whole execution in firefox, this could probably be tidied up into one method that brings in the browser
def firefox():
	driver = webdriver.Firefox()
	driver.get("http://www.facebook.com")
	email_input = driver.find_element_by_id("email")
	password_input = driver.find_element_by_id("pass")
	login_button = driver.find_element_by_id("loginbutton")
	login(email.get(),password.get(), email_input, password_input, login_button)
	visit_profile = driver.find_element_by_class_name("fbxWelcomeBoxName")
	visit_profile.click()
	ID.set(getUserID(driver.current_url))
#two methods, one for entering the credentials on the Fb homepage and one for grabbing the URL from any profile	
def login(email_address, password, email_input, password_input, login_button):	
	email_input.send_keys("%s" % (email_address))
	password_input.send_keys("%s" % (password))
	login_button.click()
def getUserID(url):	
	urlList = url.split("https://www.facebook.com/")
	return urlList[1]

#initialising the GUI    
root = Tk()
#GUI title
root.title("Facebook Personal URL Finder 3000" u"\u2122")

#initialising the GUIs attributes 
mainframe = ttk.Frame(root, padding="3 3 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#initialising some variables we'll use later
email = StringVar()
password = StringVar()
ID = StringVar()

#email input box
email_entry = ttk.Entry(mainframe, width=35, textvariable=email)
email_entry.grid(column=2, row=1, sticky=(W, E))

#password input box
password_entry = ttk.Entry(mainframe, width=35, textvariable=password, show="*")
password_entry.grid(column=2, row=2, sticky=(W, E))

#two buttons at the bottom of the screen which call the respective methods
ttk.Button(mainframe, text="Launch Chrome", command=chrome).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="Launch Firefox", command=firefox).grid(column=2, row=4, sticky=W)

#various labels used in the GUI
ttk.Label(mainframe, text="Email").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Password").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Facebook ID:").grid(column=2, row=3, sticky=W)

#this label will spit out the FB ID
ttk.Label(mainframe, textvariable=ID).grid(column=3, row=3, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

email_entry.focus()
root.mainloop()
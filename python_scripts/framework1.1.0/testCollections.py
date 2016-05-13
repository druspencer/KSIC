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
	
def sign_in():
	#TODO add code to sign in
	print "sign in"
	
def join():
	#TODO add code to join/create an account
	print "join"
	
	
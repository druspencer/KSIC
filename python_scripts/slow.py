#small module to type a given string into a given field at a given speed
#designed to imitate a human user

import time #for waits
from selenium import webdriver #for web elements
from selenium.webdriver.common.keys import Keys #for keypresses

def type_slow(self, word, input, factor): #takes in string, input field and speed factor
	for l in word: #runs a loop for how long the string is
		input.send_keys(l) #inputs the string character by character
		time.sleep(0.05*factor) #waits between entries

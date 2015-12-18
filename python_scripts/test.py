#main class, execute this from shell
#creates nested loops for browser and sites
#carries out tests on each browser/site combination
#designed for a site which has many sub-sites which you can login on

import sign_in #class which takes a target, email address and a browser and signs in
import join #class which takes a target, email address and a browser and creates a new account
import datetime #for grabbing timestamps
import os, sys #for writing to directories - only used for screenies just now

time = datetime.datetime.now() #initialises time object 
execution_time = time.strftime('%d_%m_%Y %H%M')  #grab time for various timestamps
path = 'C:/Selenium_Screenshots/'+execution_time #sets directory for this execution
os.makedirs(path) #creates above directory

targets = ["site1", "site2"] #array of sites/subsites
browsers = ["chrome", "firefox", "IE"] #array of browsers, will be used later to determine which driver to use

#nested loops
for browser in browsers:
	for target in targets2:
		join_object = join.Join() #initialises join object
		sign_in_out_object = sign_in.Sign_in_out() #initialises sign in object
		email = join_object.get_email() #calls a method from join object to set the email address for this browser/target iteration
		join_object.setUp(target, email, browser) #calls setup method for join
		join_object.test_join(path) #calls main testing method for join
		join_object.tearDown() #kills driver instance 
		sign_in_out_object.setUp(target, email, browser) #calls setup method for sign in
		sign_in_out_object.test_sign_in_out(path) #calls main testing method for sign in
		sign_in_out_object.tearDown() #kills driver instance 
		print target+" completed" #prints completed method


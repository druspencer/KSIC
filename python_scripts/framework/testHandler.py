from selenium import webdriver #for web elements
from selenium.webdriver.common.keys import Keys #for keypresses
from selenium.common.exceptions import NoSuchElementException,  WebDriverException
<<<<<<< HEAD
import reportHandler, testCollections, testCase, time
=======
import reportHandler, testCollections, testCase
>>>>>>> 5d88b0e5b0ac3f42feb4360411c27eed4680bd96

class testHandler():
	#TODO add methods which take in elements for input and clicking, checks for exceptions
	#TODO call report handler and spit out results to XML
	#TODO make each method loop a set amount of times before giving update
	#TODO each element should take a screenshot on result
	
	def __init__(self, path):
		self.report = reportHandler.reportHandler(path)
		self.tests = []
	
	def elementClick(self, element, step, expected):
		try:
			element.click()
			self.test = testCase.testCase(step, expected, "PASS", "N/A")
<<<<<<< HEAD
		except (NoSuchElementException,WebDriverException, AttributeError):
=======
		except (NoSuchElementException,WebDriverException):
>>>>>>> 5d88b0e5b0ac3f42feb4360411c27eed4680bd96
			#element not there - try again
			print "No such element - Click"
			self.test = testCase.testCase(step, expected, "FAIL", "Element Not Found")
		self.recordResults(self.test)
	
	def elementInput(self, element, input, step, expected):
		try:
<<<<<<< HEAD
			testCollections.type_slow(input, element, 1)
			time.sleep(0.5)
			#print "element text: "+element.get_attribute('value')
			assert (element.get_attribute('value') == input)
			self.test = testCase.testCase(step, expected, "PASS", "N/A")
		except (NoSuchElementException, WebDriverException, AttributeError):
=======
			utils.type_slow(input, element, 1)
			assert (element.text == expected)
			self.test = testCase.testCase(step, expected, "PASS", "N/A")
		except (NoSuchElementException,WebDriverException):
>>>>>>> 5d88b0e5b0ac3f42feb4360411c27eed4680bd96
			#element not there - try again
			print "No such element - Input"
			self.test = testCase.testCase(step, expected, "FAIL", "Element Not Found")
		except AssertionError:
			#text not there - try again
<<<<<<< HEAD
			self.test = testCase.testCase(step, expected, "FAIL", "Input Failed")
		self.recordResults(self.test)
		
	def assertText(self, element, step, expected):
	#TODO make this check if element is visible rather than text value, currently will always return true if that element is on the page rather than visible because of modals
		try:
			if element.is_displayed():
				print "element text: "+element.text
				assert (element.text == expected)	
				self.test = testCase.testCase(step, expected, "PASS", "N/A")
			else:
				self.test = testCase.testCase(step, expected, "FAIL", "Text Not Found")
		except AssertionError:
			self.test = testCase.testCase(step, expected, "FAIL", "Text Not Found")
		except AttributeError:
			self.test = testCase.testCase(step, expected, "FAIL", "Text Not Found")
		self.recordResults(self.test)
		
	def assertValue(self, element, step, expected):
	#TODO make this check if element is visible rather than text value, currently will always return true if that element is on the page rather than visible because of modals
		try:
			if element.is_displayed():
				print "element text: "+element.get_attribute('value')
				assert (element.get_attribute('value') == expected)
				self.test = testCase.testCase(step, expected, "PASS", "N/A")
			else:
				self.test = testCase.testCase(step, expected, "FAIL", "Text Not Found")
		except AssertionError:
			self.test = testCase.testCase(step, expected, "FAIL", "Text Not Found")
		except AttributeError:
			self.test = testCase.testCase(step, expected, "FAIL", "Text Not Found")
=======
			self.test = testCase.testCase(step, expected, "FAIL", "Text Not Found")
		self.recordResults(self.test)
		
	def assertText(self, element, step, expected):
		try:
			assert (element.text == expected)
			self.test = testCase.testCase(step, expected, "PASS", "N/A")
		except AssertionError:
			self.test = testCase.testCase(step, expected, "FAIL", "Text Not Found")
>>>>>>> 5d88b0e5b0ac3f42feb4360411c27eed4680bd96
		self.recordResults(self.test)
		
	def recordResults(self, test):
		self.tests.append(test)
		
	def endTesting(self, driver):
		self.report.writeResutls(self.tests)
		driver.close()
		
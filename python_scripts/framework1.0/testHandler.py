from selenium import webdriver #for web elements
from selenium.webdriver.common.keys import Keys #for keypresses
from selenium.common.exceptions import NoSuchElementException,  WebDriverException
import reportHandler, testCollections, testCase

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
		except (NoSuchElementException,WebDriverException):
			#element not there - try again
			print "No such element - Click"
			self.test = testCase.testCase(step, expected, "FAIL", "Element Not Found")
		self.recordResults(self.test)
	
	def elementInput(self, element, input, step, expected):
		try:
			utils.type_slow(input, element, 1)
			assert (element.text == expected)
			self.test = testCase.testCase(step, expected, "PASS", "N/A")
		except (NoSuchElementException,WebDriverException):
			#element not there - try again
			print "No such element - Input"
			self.test = testCase.testCase(step, expected, "FAIL", "Element Not Found")
		except AssertionError:
			#text not there - try again
			self.test = testCase.testCase(step, expected, "FAIL", "Text Not Found")
		self.recordResults(self.test)
		
	def assertText(self, element, step, expected):
		try:
			assert (element.text == expected)
			self.test = testCase.testCase(step, expected, "PASS", "N/A")
		except AssertionError:
			self.test = testCase.testCase(step, expected, "FAIL", "Text Not Found")
		self.recordResults(self.test)
		
	def recordResults(self, test):
		self.tests.append(test)
		
	def endTesting(self, driver):
		self.report.writeResutls(self.tests)
		driver.close()
		
import reportGen, os, sys

class reportHandler():
	#TODO screenshots should be saved with tests
	#TODO is a separate CSS file required?

	def __init__(self, path):
		self.path = path
		if not os.path.exists(self.path):
			os.makedirs(self.path) 
		self.xml_file = open(self.path+"/xml.xml","w")
		self.html_file = open(self.path+"/report.html","w")
		reportGen.createHTML(self.html_file)
		reportGen.createXML(self.xml_file)
		self.xml_file.close()
		self.html_file.close()
	
	def writeResutls(self, tests):
		self.xml_file = open(self.path+"/xml.xml","a")
		for test in tests:
			self.xml_file.write("""	<ENTRY>
		<STEP>%s</STEP>
		<EXPECTED>%s</EXPECTED>
		<RESULT>%s</RESULT>
		<CONDITIONS>%s</CONDITIONS>
	</ENTRY>""" %(test.step, test.expected, test.result, test.result_conditions))
		self.xml_file.write("""
</CATALOG>
""")

		
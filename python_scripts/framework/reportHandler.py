import reportEmail, os, sys, smtplib

class reportHandler():
	#TODO screenshots should be saved with tests
	#TODO is a separate CSS file required?
	#TODO email results?

	def __init__(self, path):
		self.path = path
		self.content = ""
		self.html_str = ""
		if not os.path.exists(self.path):
			os.makedirs(self.path) 
	
	def writeResutls(self, tests):
		#self.xml_file = open(self.path+"/xml.xml","a")
		for test in tests:
			self.content+=("""<tr class ="%s">
	<td> %s </td>
	<td> %s </td>
	<td> %s </td>
	<td> %s </td>
</tr>"""%(test.result, test.step, test.expected, test.result, test.result_conditions))
		self.composeFile()
		self.postResults()
	
	def sendEmail(self):
		#Specifying variables
		fromaddr = ''
		toaddrs  = ''
		subject = 'Test Results'

		#Construct the message with headers and content
		msg = """From: Laurie Green <%s>
To: %s
Subject: %s
MIME-Version: 1.0
Content-type: text/html

%s"""%(fromaddr,toaddrs,subject,self.html_str)

		#Gmail Login
		username = ''
		password = ''

		#Sending the mail  
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(fromaddr,password)
		server.sendmail(fromaddr, toaddrs, msg)
		print "sent"
		server.quit()
	
	def composeFile(self):
		self.html_str = """
<!DOCTYPE html>
<html>
<style>
table,th,td 
{
	border : 1px solid black;
	border-collapse: collapse;	
	margin-right: auto;
	margin-left: auto;
	font-family: arial;
	color: black;
}
th,td 
{
	padding: 5px;
}
th
{
	background-color: grey;
}
body
{
	background-color: white;
}
.PASS{
	background-color: green;
}
.FAIL{
	background-color: red;
}


</style>
<body>
<br>
<br>
<table id="results">
	<tr>
		<th>Step</th>
		<th>Expected</th> 
		<th>Result</th>
		<th>Conditions</th>
	</tr>
	%s
</table>
</body>
</html>
"""%(self.content)

	def postResults(self):
		html_file = open(self.path+"/report.html","w")
		html_file.write(self.html_str)
		html_file.close()
		self.sendEmail()

		
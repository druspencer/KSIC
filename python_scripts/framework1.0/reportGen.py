def createHTML(html_file):
	html_str = """
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
	font-variant: small-caps;
	color: white;
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
	background-color: black;
}

</style>
<body>
<br>
<br>
<table id="results"></table>

<script>
function loadXMLDoc() 
{
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() 
	{
		if (xmlhttp.readyState == 4 && xmlhttp.status == 200) 
		{
			populateTable(xmlhttp);
		}
	};
	xmlhttp.open("GET", "xml.xml", true);
	xmlhttp.send();
}
function populateTable(xml) 
{
	var i;
	var xmlDoc = xml.responseXML;
	var table="<tr><th>Step</th><th>Expected</th><th>Result</th><th>Conditions</th></tr>";
	var x = xmlDoc.getElementsByTagName("ENTRY");
	for (i = 0; i < x.length; i++) 
	{ 
		table += "<tr><td>" +
		x[i].getElementsByTagName("STEP")[0].childNodes[0].nodeValue +
		"</td><td>" +
		x[i].getElementsByTagName("EXPECTED")[0].childNodes[0].nodeValue +
		"</td><td>"+
		x[i].getElementsByTagName("RESULT")[0].childNodes[0].nodeValue +
		"</td><td>"+
		x[i].getElementsByTagName("CONDITIONS")[0].childNodes[0].nodeValue +
		"</td></tr>";
	}
	document.getElementById("results").innerHTML = table;
}
function colourResults()
{	
	var rows = document.getElementById("results").rows;
	for (i=0; i< rows.length ; i++ )
	{
		if (rows[i].cells[2].innerHTML == "PASS")
		{
			rows[i].style.backgroundColor = "green";
		}
		if (rows[i].cells[2].innerHTML == "ALERT")
		{
			rows[i].style.backgroundColor = "yellow";
		}
		if (rows[i].cells[2].innerHTML == "FAIL")
		{
			rows[i].style.backgroundColor = "red";
		}
	}
	
}
loadXMLDoc();
setTimeout(colourResults, 50);
</script>
</body>
</html>
"""

	html_file.write(html_str)
	html_file.close()

def createXML(xml_file):
	xml_str = """<?xml version="1.0" encoding="UTF-8"?>
<CATALOG>	
"""
	xml_file.write(xml_str)
	xml_file.close()
<html>

<body>

Hello There

<%
	Response.Write "The time is " & Time()

	x = 5
	If x > 3 Then
		Response.Write "<p> x is greater than 3 </p>"
	Else 
		Response.Write "<p> x is not greater than 12 </p>"
	End If

	' mod
	MyValue = 10 MOD 3

	' round to 2 decimal places
	MyValue = Round(10 / 3, 2)

	' date and time
	MyHour = DatePart("h", #8:00 pm#)

	response.write MyHour  ' 20

%>

<p> 
	Go to my <a href="../index.html"> home page </a>
</p>

<form method="POST" action="ASP.asp">
	<p>	
		Customer Name: 
		<input type="text" name="CustomerName">
	</p>
	<p>
		Customer Age:
		<input type="text" name="CustomerAge">
	</p>
	<p>
		<input type="submit" value="Submit" name="submit">
	</p>
</form>

<%	
	' take request from form
	CustomerName = Request("CustomerName")
	CustomerAge = Request("CustomerAge")

	Response.Write "Hello" & CustomerName
	Response.write ", You are " & CustomerAge & " old."


	' Query string, http://www.path.com?key1=value1&key2=value2&key3=value3
	' e.g. http://www.path.com?firstname=Alice&lastname=Smith
	queryString = Request.Querystring
	' read from query string, store the value of key1
	Referer = Request("key1")

%>


<!-- shortcut to resonse.write() -->
<%="Hello World"%>


<!-- build HTML tags -->
<%
	Response.Write "<h2> example of building html tags </h2>"
%>


<!-- build HTML tags with attribute -->
<%
	Response.Write "<p style='color:red'> Some Text </p>"
%>


<!-- convert to uppercase and lowercase -->
<%
	name = "Alice Smith"
	Response.Write ucase(name)  		' ALICE SMITH
	Response.Write lcase(name)  		' alice smith
%>


<!-- reverse a string -->
<%
	text = "Hello"
	Response.Write strReverse(text) 	' olleH
%>


<!-- round a number -->
<%
	number = 1.23
	Response.Write Round(number)		' 1
	number = 1.6
	Response.write Round(number)		' 2
%>


<!-- generate a random number -->
<%
	Randomize()
	Response.Write(rnd())				' a random float 0 <= number < 1
%>


<!-- generate a random int -->
<%
	Randomize()
	random_int = Int(100 * rnd)
	Response.Write(random_int)			' a random int between 0 and 99
%>


<!-- find substring -->
<%
	text = "abcde"
	Response.write left(text, 3)		' "abc"
	Response.Write right(text, 2) 		' "de"
	' string starts with index 0 in VB script
	' Mid(string, start_index, number_of_characters)
	Response.Write Mid(text, 3, 2)		' "cd"	
%>


<!-- replace context in a string -->
<%
	text = "abcde"
	Response.Write Replace(text, "ab", "xy") 	' "xycde"
%>



<!-- form with method=get -->
<form action="asp.asp" method="get">
	Your name: 
	<input type="text" name="name">
	<input type="submit" value="submit">
</form>
<!-- process submitted form -->
<!-- action="asp.asp" specifies the destination, 
	i.e. where we submit this form to -->
<%
	name=Request.QueryString("name")
	If name <> "" Then
		Response.Write("Hello " & name)
	End If
%>


<!-- form with method=post -->
<form action="asp.asp" method="post">
	Your name:
	<input type="text" name="name">
	<input type="submit" value="submit">	
</form>


<!-- year function -->
<%
	response.write year(date) 			' prints year of date, i.e. 2017
	response.write year("2016-02-02")	' prints 2016
%>


<!-- execute a stored porcedure -->
<%
	Dim objConnection, objRS, strSP
	call DBOpen(objConnection, objRS)
	strSP = "Excc str_nameOfStoredProcesure argument1 argumetn2"
	objConnection.Execute
%>


</body>
</html>







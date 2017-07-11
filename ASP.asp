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



</body>
</html>
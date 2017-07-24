
Module Module1

	sub Main()								' all programs must have Main()

		Console.WriteLine("Hello World")	' print, new-line character included
		Console.Readline()					' wait for user input

		Dim myNum As Integer				' declare variable myNum as an integer
		myNum = 5							' set myNum equalt to 5

		Dim myDouble As Double = 3.14		' declare and define a double
		Dim myBool As Boolean = False 		' declare and define a boolean

		' NULL value in VB, prevents crush from accessing a no-value variable
		Dim myNull As Integer = Nothing		' None in Python
		Console.WriteLine(myNull)			' will not crash

		' declare and define a string
		Dim myString As String = "Hello new boston fans" 
		' if statement, = for equality, <> for inequality, other as usual
		If myVar = "something" Then
			Console.WriteLine("myVar")
		ElseIf myNull = "something else" Then
			Console.WriteLine("in else if")
		Else
			Console.WriteLine("in else")
		End If

		' logical operators 
		Console.WriteLine(True And False)
		Console.WriteLine(True Or False)
		Console.WriteLine(Not False)

		' string concatenation in console.WriteLine
		Console.WriteLine("string 1" & "string 2")	' must use &
		Dim myStr As String = "str1" + "str2"		' must use +

		' String methods

		' get string length, don't use "abc".Length
		Dim myStrLength As Integer = Len("abc")			' result = 3

		' return 3 characters, from index 1 and onwards, 
		Dim myStr As String = "welcome".Substring(1, 3)	' result = "elc"
		' return first 3 characters
		Dim myStr As String = "welcome".Substring(3)	' result = "wel"

		' remove leading and trailing white spaces
		Dim TestString As String = "  <-Trim->  "
		result = LTrim(TestString)			' Returns "<-Trim->  ".
		result = RTrim(TestString)			' Returns "<-Trim->".
		result = LTrim(RTrim(TestString))
		' Using the Trim function alone achieves the same result.
		TrimString = Trim(TestString)		' Returns "<-Trim->".

		' more string methods: 
		' https://docs.microsoft.com/en-us/dotnet/api/microsoft.visualbasic.strings?view=netframework-4.7#methods_'

		' select case, no breaks
		Dim myInt As Integer = 5
		Select Case myInt
			Case 0
				Console.log("in case 0")
			Case 1
				Console.log("in case 1")
			Case myInt < 10					
				Console.log("in < 10")		' boolean expression is allowed'
			Case Else
				Console.log("all other cases")
		End Select

		' declare an array of length 3
		Dim myArray(2)			' 3 is the ending index of this array
		myArray(0)	= "first"
		myArray(1) = "second"
		myArray(2) = "third"

		' preserve the content of my array and change length
		ReDim Preserve myArray(4)

		' clear the entire array and re-set it's length
		ReDim myArray(4)	



		' alternative way
		Dim strArray() As String = {"first str", "second str", "third str"}

		Array.Sort(myArray)		' sort array
		Array.Reverse(myArray)	' reverse array

		' Loops
		' normal for each loop
		For Each item As String in myArray
			' do something to item
		Next

		' normal for loop, it runs from 1 to 20 inclusively
		For i = 1 To 20 Then
			'` do something here'
		Next

		' skip 5 itnegers at a time
		For i = 1 To 20 Step 5
			'` do something here'
		Next

		' break and continue
		For i = 1 To 20 Then
			' continue
			If i < 5 Then
				Continue For
			End If

			' break
			If i = 15 Then
				Exit For
			End If
		Next

		' Do While loop, Normal while loop
		Dim num As Integer = 0	'loop stos when num > 15
		Do While num <= 15
			num += 1
		Loop


		' Do Until Loop, keep looping until condition is True
		Dim num As Integer = 0
		Do Until num = 15		' loop stops when num = 15
			num += 1
		Loop

		' Do Until Loop, do the task at least once, then enter condition
		Dim num As Integer = 0
		Do
			num += 1
		Loop Until num = 15			' also works for Loop While

		' define a constant
		Public Const MYVALUE AS INTEGER = 1	' accessibility can be Private

		' change variable type
		Dim myVar As Integer = 1
		Dim convertedVar As Boolean = CType(myVar, Boolean)

		' enumeration
		Private Enum DayAction As Integer
			Awake = 0
			Asleep = 1
			Coding = 2
		End Enum

		' enumeration, get name by value
		System.Enum.GetName(GetType(DayAction), 2) ' print coding

		' enumeration, is defined
		System.Enum.IsDefined(GetType(DayAction), "Coding") ' Print True

		' 0 -> "Awake", 1 -> "Asleep", 2 -> "Coding"
		Private action As DayAction = 1		
		MessageBox.show(action.ToString()) 	' 1 -> "Asleep"

		' alternative way, set it directly
		Private action As DayAction = DayAction.Awake
		MessageBox.show(action.ToString()) 	' print Awake

		' getters, setters and date time picker
		Private Property Hour() As Integer
			Get
				Return dtpHour.Value.Hour
			End Get
			' Now represents current system time
			' Date(year, month, day, hour, minute, second)
			Set(ByVal value As Integer)
				dtpHour.Value = New Date(Now.Year, Now.Month, Now.Day, value, 0, 0)
			End Set
		End Property

		' special format, #month/day/year# 
		Dim currentDate As Date = #10/20/2017#

		' define and initialize a structure
		Private Structure Customer
			' public fields
			Public FirstName As String
			Public LastName As String
			Public Email As String

			' property is a dynamiccly computed field
			Public ReadOnly Property Name() As String
				Get
					Return FirstName & " " & LastName
				End Get
			End Property

			' method overriding
			Public Overrides Function ToString() As String
				Return Name & " (" & Email & " )"
			End Function

			' random
			Dim generator As New Random
			' generator a number between 0 and 20 inclusively
			Dim randonInt = generator.Next(0, 20)		


		End Structure

		' c
		Private myCustomer As Customer
		myCustomer.FirstName = "Alice"
		myCustomer.LastName = "Smith"
		myCustomer.Email = "alice.smith@cefi.ca"



		' array list, holds data with different types
		Private myCustomers As New ArrayList
		myCustomers.Add(myCustomer)
		myCustomers.Add(1)
		myCustomers.Add("string")
		myCustomers.Remove("string")	' remove first occurence
		myCustomers.RemoveAt(1)			' remove element by index

		' append elements in myArray into myCustomers
		Private myArray() As String = {"Alice", "Bob", "Charlie"}
		myCustomers.AddRange(myArray)

		' Queue is a built-in type in VB
		Private myQueue As New Queue
		myQueue.Enqueue("first")
		myQueue.Enqueue("second")
		myQueue.Enqueue("third")
		myQueue.Dequeue()	' return and remove "first"
		myQueue.Peak()		' return "second" without mutating myQueue

		' Stack is a built-in type
		Private myStack As New Stack
		myStack.push("first")
		myStack.push("second")
		myStack.pop()		' return and remove "second"
		myStack.peek()		' return "first" without mutating myStack

		' 2D array
		Private multiArray(1, 2) As String

		multiArray(0, 0) = "position 0 0"
		multiArray(0, 1) = "position 0 1"
		multiArray(0, 2) = "position 0 2"
		multiArray(1, 0) = "position 1 0"
		multiArray(1, 1) = "position 1 1"
		multiArray(1, 2) = "position 1 2"

		' temporarily create a variable, myVar is destroyed after End Using
		Using myVar = 5
			Console.WriteLine(myVar)
		End Using


		' file IO, StreamWriter
		Imports System.IO
		' sample path: "G:\myFile.txt"
		Private myWriter As New StreamWriter("path to file")
		myWriter.WriteLine("hello world!")
		myWriter.Close()

		' file IO, StreamReader
		Private fileToLoad As New StreamReader("path to file")
		Dim fileContent As String = fileToLoad.ReadToEnd()

		' file IO, FileStream
		' open file for writing
		Private fileStream As FileStream = File.OpenWrite("path to file")
		' read entire file and store content in fileContent
		Dim fileContent As String = File.ReadAllText("path to file")

		' special directories, read a.txt on desktop
		File.ReadAllText(My.Computer.FileSystem.SpecialDirectories.Desktop + "\a.txt")

		' special directories, read a.txt on desktop
		File.ReadAllText(My.Computer.FileSystem.SpecialDirectories.Desktop + "\a.txt")

		' change the visibility of a file to hidden
		File.SetAttributes("path to file", FileAttributes.Hidden)

		' try catch
		Try
			' some code here
		' catch specific exception
		Catch ex As IndexOutOfRangeException
		' catch specific exception under certain condition
		Catch ex As IndexOutOfRangeException When "some conditions"
		' catch all exception
		Catch
			Console.WriteLine("error occured and caught")
		Finally
			' optional, do something here
		End Try

		' throw exception
		Dim maxIndex = 5
		Dim currentIndex = 0
		If currentIndex > maxIndex Then
			Throw IndexOutOfRangeException
		End If
	end sub


End Module


' Define a form
Public Class Form1
	Private Sub btnMyButton_Click()
		MessageBox.Show("actual message", "name of pop-up window")
	End Sub
End Class

' Define a function
' ByVal = pass by value, 
Private Function addNums(ByVal num1 As Double, ByVal num2 As Double) As Double
	return num1 + num2
End Function

' ByRef = pass by reference, this will update global variable num
' By default, VB pass variables by ref
Private Sub increment(ByRef num As Integer)
	num += 5	' no return needed
End Sub

' using optinal variable, key word Optional and default value must be used together
Private Sub optional(Optional ByVal message As String = "default value")
	MessageBox.show(message)
End Sub

' functions with different signature, AKA coercion
Private Sub showType(ByVal num As Integer)
	MessageBox("this is a integer")
End Sub
Private Sub showType(ByVal num As Double)
	MessageBox("this is a double")
End Sub

' pass array as parameter
' arrayArray() As String is a string array
Private Sub AddItemsToList(ByVal argArray() As String)

' exit a sub
Private Sub()
	While True
		num += 1
		If num > 10 Then
			Exit Sub
		End If
	End While
End Sub

' class
Public Class Person
	Public weight As Double = 100
	' this is a class variable, all Person objects will share the same
	' minWeight variable, change to minWeight will affect all Person objects
	Public Shared minWeight = 0		

	Sub New(ByVal newWeight As Double)
		weight = newWeight
	End Sub

	Public Sub eat(ByVal pounds As Double)
		weight += pounds
	End Sub

	Public Sub exercise(ByVal time As Double)
		weight -= time
	End Sub

	' getter
	Public Sub getWeight() As Double
		Return weight
	End Sub
End Class



' With create a short form equivalent to 
' myPerson.weight = 100
' myPerson.eat()
Dim myPerson As New Person
With myPerson
	.weight = 100
	.eat()
End With

' inheritance
Public Class Professor
	Inherits People
End Class


' create new namespace
' having multiple namespaces is similar to having multiple files
Namespace myNamespace
	' some code
End Namespace

' error handler
Sub ResumeStatementDemo()
	' Enable error-handling routine.
	On Error GoTo ErrorHandler   
	Dim x As Integer = 32
	Dim y As Integer = 0
	Dim z As Integer
	z = x / y   ' Creates a divide by zero error
Exit Sub   ' Exit Sub to avoid error handler.

' Error-handling routine.
ErrorHandler:
	' Evaluate error number.
	' table of error flags
	' https://msdn.microsoft.com/en-us/library/aa264975(v=VS.60).aspx
	Select Case Err.Number   
		Case 6   ' 6 == Divide by zero error.
			y = 1 ' Sets the value of y to 1 and tries the calculation again.
		Case Else
			' Handle other situations here....
	End Select
	' Resume execution at same line
	Resume   
End Sub

' if option explicit or option explicit on
' then all variable must have dim or redim
Option Explicit
Option Explicit On

' option explicit off will allow defining variable without dim
Option Explicit Off
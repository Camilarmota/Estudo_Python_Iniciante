## print is a function used to display a value on the screen;
## Quotation marks mark the beginning and end of a value, a string.
print ("Hello, World! This is my first program in Pyhon")
print ("Date: Friday, October 25th, 2024.")
## The type function can tell you the class of the value, Data type.
type ("My name is Camila")
type (2024)
## Strings belong to the class str.
## Integers belong to the class int. 
## Numbers with a decimal point belong to a class called float.
## Use triple quoted strings when use multiple lines:
message = """ My name is Camila.
I'm enjoying studying Python.
I want to become a data scientist. """
print (message)
## message is a variable.
## len is a built-in Python function that returns the number of characters in a string, example:
x = len("hello")
## return 5
## When a variable name appears in the place of an operand, it is replaced with its value before the operation is performed.
## Example: so let us convert 645 minutes into hours:
minutes = 645
hours = minutes / 60
hours
## To return an integer value when dividing, two slashes are used //, called floor division.
## The functions int, float and str, can be used to convert their arguments into types int, float and str respectively.
## Example: 
int (192,50)
## Will return the number 192.
## The + operator does work with strings, but for strings, the + operator represents concatenation, not addition.
## Example: 
name = "Camila"
last_name = " Mota"
print(name + last_name)
## The output of this program is Camila Mota.
## When you want a string to be repeated, use * followed by the number of repetitions.
## The function imput creates a dialog
## Example: 
n = input("Please enter your name: ")

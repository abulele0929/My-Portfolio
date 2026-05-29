#type casting = is the process of converting a value from one data type to another. 
# Example of type casting
x = 1
y = 2.5
z = "3"

int(y)  # Output: 2. Converts the float 2.5 to the integer 2 by truncating the decimal part.
str(x) # Output: "1". Converts the integer 1 to the string "1".
float(z)  # Output: 3.0. Converts the string "3" to the float 3.0.

# f-string 
# f-string = is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}
# This type of string formatting makes it easier to create formatted strings by directly including variables and expressions within the string.
# It can be used instead of type casting to convert data types within a string.

# Example of f-string
name = "Alice"
age = 15
height = 1.75
# Using f-string to format the string with variables

# Instead of printing the code like this:
# print("My name is " + name + " and I am " + str(age) + " years old and my height is " + str(height) + " meters.")

# Using f-string to format the string with variables
print(f"My name is {name} and I am {age} years old. My height is {height} meters.")
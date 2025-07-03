# If you want to print ant output we use Print function for that
print("Hello,World")

# print is a function and the string in the paranthesis is argument.Python use only one line argument

print("Hello")
print("World")

# it has default newline char by that second print argu goes in next 
# Escape and Newline char(\n): Where we use newline char there appear newline 
print("My college name is\ngla university")

#if i want to print my arg in same line then we use end="" we can assign a letter space or nothing .
# it has default \n if we dont use anything
print("My name is", "Python.", end=" ")
print("Monty Python.")
 #output: My name is Python. Monty Python.

#keyword arg:sep(default it is empty )
print("My", "name", "is", "Monty", "Python.", sep="-")
#Output: My-name-is-Monty-Python.

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
# Output: My_name_is*Monty*Python.*
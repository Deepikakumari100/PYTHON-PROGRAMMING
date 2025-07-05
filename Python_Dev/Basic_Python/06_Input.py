var=input("Tell me anything:")
print(var)
# the result of the input() function is a string.
# If we want to take integer, float as input then we use int(),float() ex:
var=int(input("Enter the number"))
print(var)
var=float(input("Enter the float number"))
print(var)

# find the hypotaneous
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", round(hypo,2)) # We can use round function to set the limit of decimal upto

# The + (plus) sign, when applied to two strings, becomes a concatenation operator:
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# string * number
# number * string
# It replicates the string the same number of times specified by the number.

# For example:

# "James" * 3 gives "JamesJamesJames"
# 3 * "an" gives "ananan"
# 5 * "2" (or "2" * 5) gives "22222" (not 10!)
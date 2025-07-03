# integers, those which are devoid of the fractional part
#  1,2,3 etc
print(1,2,3)

# floating-point numbers , that contain  the fractional part.
#1.2,1.3, 2.44 etc
print(0.4,1.2)

# if an integer number is preceded by an 0O or 0o prefix (zero) sufix(english letter O), it will be treated as an octal value.
print(0o123)

# Hexadecimal numbers: Such numbers should be preceded by the prefix 0x or 0X (zero-x).
print(0x123)

# Boolean values: True or False
print(3>2)
print(2<3)

#String : strings need quotes. This is a very typical string: "I am a string."
print("I am a String.")

#Binary: a binary number is made up of 0s and 1s only, e.g., 1010 is 10 in decimal.
a=bin(10)
print(a)
print(int(a,2)) #this will convert it binary to integer 2 is for telling we gave a binary number.

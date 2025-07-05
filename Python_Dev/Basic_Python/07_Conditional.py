# if condition:
sheep_counter=int(input())
if sheep_counter >= 120:
    print("Fall Asleep")
print("Go for a walk") # This function is not indented and does not belong to the if block, which means it is always executed.


#If-Else Condition:
# if true_or_false_condition:
#     perform_if_condition_true
# else:
#     perform_if_condition_false

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
# if number1 > number2:larger_number = number1
# else: larger_number = number2  :> we can write them like this also.

print("The larger number is:", larger_number)



# Nested If-Else Statement:
a=int(input("Enter your Marks"))
if a>30:
    if a>70:
        print("We got good grade")
    else:
        print("We are just pass")
else:
    if a<25:
        print("We are 100percent  fail")
    else:
        print("We still have chance to pass")


# ELIF Statements:
b=int(input("Enter your marks: "))
if b>30:
    print("You are pass")
elif b>50:
    print("You got B grade")
elif b>70:
    print("you got A grade")
elif b>90:
    print("you got O grade")
else:
    print("Your Result Not Found")
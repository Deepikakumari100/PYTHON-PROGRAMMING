#1. if
a=int(input("Enter the Number "))
if a%2==0:
    print(a,"is Even Number")

#2. if-else
else:
    print(a,"is Odd Number")

#3. if-elif-else
marks=int(input("Enter the Marks "))  
if marks>=60:
    print("Pass with first div.")
elif marks>=45:
    print("Pass with Second div.")
elif marks>=33:
    print("Pass with third div.")
else :
    print("Fail")        
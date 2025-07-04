# Format() method formats the specified value(s) and insert them inside the string's placeholder '{}'.
# Named indexes
txt1="Welcome to {fname} {lname}".format(fname='VS',lname='Code')
print(txt1)
# Numbered indexes
txt2="Welcome to {0} {1}".format("VS",'Code')    
print(txt2)
# Empty placeholder
txt3="Welcome to {} {}".format("VS",'Code')
print(txt3)
# ques.>
w="Welcome {b:10} to {a} VS code".format(a=30,b=40)        #here{b:10} represents that b has has 10 character space, and we have b=40 so o/p=        40(have 8 spaces 40 so total 40)
print(w) # you can also use {b:>10} this but {b:10} also by default give the left space
w="Welcome {b:<10} to {a} VS code".format(a=30,b=40)
print(w)   #{b:<10} give the right space
w="Welcome {b:^10} to {a} VS code".format(a=30,b=40)
print(w)   #{b:^10} place the value in between
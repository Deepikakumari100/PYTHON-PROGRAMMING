# List Comprehension is an elegant way to create list. More compact and faster then normal functions and loops for creating a list.
# Syntex :- [expression for item in list]
# Normal way
l=[]
print("By Normal way :")
for i in range(1,101):
    l.append(i)      # append used for adding element in list 

print(l) 

# List comprehension
print("By List Comprehension : ")
n=[a for a in range(1,101)]
print(n)

# ques.> print all even numbers from 1 to 100
n=[e for e in range(1,101) if e%2==0]      # here 'if' is used for filter(giving condition)
print(n)

# ques.> convert string into list
s='hello'
l=[a for a in s]
print(l) 
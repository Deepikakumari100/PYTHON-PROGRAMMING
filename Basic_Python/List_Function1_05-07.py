# 1. Function for Deleting element in list
# i. del :- delete through index
l=[10,20,30,40,50]
del l[2]
print(l)

# ii. pop() :- delete through index and it can also return the deleted value
l=[10,20,30,40,50]
print("Deleted no. :- ",l.pop(2))
print(l) 

# iii. remove() :- it delete through value
l=[10,20,30,40,50]
l.remove(50)
print(l)

# iv. clear() :- blank the entire list. o/p=[]
l=[10,20,30,40,50]
l.clear()
print(l)

# 2. Fuctions for updating element in list
l=[10,20,30,40,50]
l[0]=1
print(l)

# i. insert() :- for inserting the value at any position
l=[10,20,30,40,50]
l.insert(0,100)   # 0> index and 100>value that i want to insert
print(l)  #l[0]=100,l[1]=10,l[2]=20,........

# ii. append() :- add the element at end(last) of the list
l=[10,20,30,40,50]
l.append(60)
print(l)

# iii. extend() :- list ke andar ki value ko le kar list m add kar deta hai
l=[10,20,30,40,50]
n=[60,70]
l.extend(n)
print(l)
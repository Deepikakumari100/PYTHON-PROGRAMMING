l=[10,20,30,40,10]
# 1. count() :- used for counting the element
c=l.count(10)
print(c)

# 2. max() :- return the maximum value of the list
m=max(l)
print(m)
n=['Hello','World']
ma=max(n)
print(ma)   # o/p = World because W comes after H. 

# 3. min() :- return the minimum value of the list
mi=min(l)
print(mi)
mn=min(n)
print(mn)

# 4. sort() :- sort the values in ascending or descending order 
l.sort()
print(l)

# 5. reverse() :- reverse the list
l=[10,67,20,30,40,2]
l.reverse()
print(l)

# 6. index() :- it will give the value through index number
l=[10,67,20,30,40,2]
i=l.index(67)
print(i)
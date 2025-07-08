# Zip Function :- used to Iterate Over 2+ Lists at the Same Time.
l=[10,20,30,49]
l1=[9,88,0,56]

for a,b in zip(l,l1):   # here we take two varibles a,b to store the elements of l and l1 resp.
    print(a,b)          # it will only print until the list have the same number of elements like list1 have 4 elements and list2 have 5 then it will not print the 5th element.

# without zip function
t=len(l)
for h in range(t):
    print(l[h],l1[h])    

l=[10,20,30,40,50,60]
# List_Iteration by for loop
t=len(l)
for i in range(t):
    print(l[i])      # by using this we get value one by one like first, l[0]=10 then l[1]=20 and so on.
# > for loop by direct passing the list
for a in l:
    print(a)
# ques.> print the list in reverse order.
print("List in reverse order :")
for i in range(t-1,-1,-1):
    print(l[i])    
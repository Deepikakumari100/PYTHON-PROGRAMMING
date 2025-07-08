# for single input
n=input("Enter the string :-")
t=n.split()        # split():- used for breaking the string from the spaces.
print("List is :-",t)

# for multiple strings
l=[]
for a in range(1,4):
    n=input("Enter the String(value)"+str(a)+":-")
    l.append(n)
print("Final List is :-",l)
# A String is sequence of charachters
# STRING_INDEXING
print("STRING_INDEXING :")
s="welcome to vscode"
print(s[5])
print(s[-1])
print(s[-4])

# STRING_SLICING            [start:stop:step]
print("STRING_SLICING :")
print(s[0:7])
print(s[-1])
print(s[-1::-1])

# STRING_ITERATION
t=len(s)
print(t) #17
for i in range(t):
    print(s[i])       # s[0]=w , s[1]=e ,.....

print("Reverse the string..")
rev=s[-1::-1]         # reverse
for i in range(t):
    print(rev[i])
# OTher method
print("OR")
for i in range(t-1,-1,-1):
    print(s[i])    
print()

# direct string pass
for i in s:
    print(i)    
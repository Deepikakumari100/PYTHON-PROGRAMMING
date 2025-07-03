# range(5)
# start=0 (Default)
# condition<5
# increment=1 (Default)

# range(1,5)
# start=1
# condition<5
# increment=1 (Default)

# range(1,6,2)
# start=1
# condition<6
# increment=2

# FOR_LOOP
# ques.> print 2's table
for i in range(1,11):
    print("2 X ", i ," = ",2*i)
# ques.> print reverse number from 10 to 1    
for i in range(10,0,-1):
    print(i)

# WHILE_LOOP   
# >Start
# >Condition
# >Increment/Decrement 
i=1                                      #Start
while i<=10:                             #Condition
    print(i," Welcome to VS Code!")       
    i+=1                                 #Increment

print(i)                   # o/p =11 becoz last value of i=11 becoz after 10 loop will stop , so at last i=11
 
a=10
while a>=1:
    print(a,"hello!!!") 
    a-=1
print(a)                  # o/p=0    
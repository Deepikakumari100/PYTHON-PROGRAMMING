# List '[]' is a mutable data type. you can create or take int, string, list, tuple,dictionary inside list and list is comma ',' sepreated.
l=[1,2,3,4,5]    # integer list
print(type(l))
# ques.> to get 3 from the list
print(l[2])
# nested list : list inside the list is called nested list
nl=[1,2,3,[4,5,6]]    # here '[4,5,6]' is a nested list and index number is like '1'=0,'2'=1,'3'=2 and '[4,5,6]'=3. [4,5,6] will take as single element .
print(nl[3])
# ques.> to get 5 form the nested list
print(nl[3][1])
# mixed list(include number,string,list)
ml=[1,2,'String',[3,4,5]]
# ques.> to get String from ml
print(ml[2])
# List_Slicing
print(ml[0:2])     # stop before index number=2. [start:stop:step]
print(ml[1:])
# ques.> get 1,String from ml
print(ml[0::2])
# or by reverse indexing
print(ml[-2::-2])
#1.Number
a=5
print(a,type(a))   #i. int
a=5.5
print(a,type(a))   #ii. float
a=2+5j
print(a,type(a))   #iii. complex

#2.Sequence Type
#i. String(sequence of any character) : is a collection of one or more characters put in a single,double and tripal quote. Multiline string can be denoted using tripal quote
s='Hello!1234'
print(s,type(s))
s='''
  Hello,
  you stupid!
'''
print(s,type(s))
s='10' 
print(s,type(s))

#ii. List (oredered sequence of items):it is most used and flexible . List is MUTABLE
l=[10,'ws',9.5]
l[2]=20      #MUTABLE :- list,Dictonary,byte array
print(l,type(l))

#iii. Tuple (oredered sequence of items same as list) .Tuple is fast
t=(10,20,'Hello')
print(t,type(t))
t1=(10)   # int datatype because only one item , hence it return the datatype of that value
print(t1,(type(t1)))
print(t[0])

#3. Dictionary (unordered collection of key:value pair)
d={
    'course_name':'Python',
    'course_duration':'2 Months'
}
print(d['course_name'])
print(d,type(d))

#4. Set (unordered collection of items): every set element is unique(no duplicates),means no repitation of values and must be immutable(cannot change)
s={10,20,30,10} # it remove 2nd 10 because no repitation of value allowed
print(s,type(s))
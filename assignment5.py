from math import *
import functools
import operator
import sys
#question 1
numbers=[i%2!=0 for i in range(1,1300)]
print(numbers)
#question 2
lis=range(1,10)
print("the multiplication of list elementsis:",end="")
print(functools.reduce(operator.mul,lis))
#question 3
def game(func):
    def inner(*args,**kwargs):
        print("hello, this is before function execution")
        returned_value=func(*args,**kwargs)
        return returned_value
    return inner
def helpme(a,b):
    print(" sum is:",a+b)
    
helpme(8,9)


#Question 4
def file_read(fname):  
    with open(fname,'r')as f:
        words=f.read().split()
        max_length=len(max(words, key=len))
        return [word for word in words if len(word)==max_length]
print(file_read('text.txt'))
def file_r(fname):
    value=[]
    with open(fname) as f:
        for line in f:
            value.append(line)
            print(value)
file_r('text.txt')
#question 5
class Triangle:
    
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def area(self):
        s=(self.a+self.b+self.c)/2
        return (s*((s-self.a)*(s-self.b)*(s-self.c)))**0.5
a=int(input("Enter the value of a = "))
b=int(input("Enter the value of b = "))
c=int(input("Enter the value of c= "))
obj=Triangle(a,b,c)
print(obj.area())

 #question 6
import random
import string
seen=''
i=0
random=''.join([random.choice(string.ascii_letters+string.punctuation+string.digits)for n in range(30)])

for x in random:
    if random.index(x)==i:
        seen+=x
    i+=1
print(seen)
       
#question 7
def new_list():
    a=[23,12,15,18,19,10]
    
    res=[a[i] for i in (0,-1)]
    return res
new_list()
print(new_list())

#question 8
def oddeven():
    a=[21,31,45,54,62,67,89]
    b=[43,57,60,91,22,30,12]
    l=[]
    count=0
    for i in a:
        if count%2==1:
            l.append(i)
        count+=1
    for j in b:
        if count%2==0:
            l.append(j)
        count+=1
        
    
    return l
oddeven()
print(oddeven())
    

#question 9
my_list=[1,2,3,4,5,6,7,8,9,10]
def divide_chunks(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]
n=3

x=list(divide_chunks(my_list,n))
for i in [x]:
    for j in i:
        print(j[::-1])

#question 10
x=[1,2,3,4]
dic={'a':10,'b':2,'c':40,'d':30}
for i in x:
    for k,v in dic.items():
       if i==v:
            print('x=',[i])



            
    
 


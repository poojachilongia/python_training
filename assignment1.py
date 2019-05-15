#question 1
x = int(input("enter number"))
print( "You have entered",x)
type(x)
#questsion 2
x=input("enter name")
print("hello! my name is ",x)

"Hello I am a candidate" 
x="hello i am a candidate"
print(x)

"234.56"
x="234.56"
print(x)
type(x) 

"34" 
x=input ("enter value")
print(x)
type(x)

#question 3
x= 10+20*(45+67.0) 
print(x)
type(x)

x= bool(True and False)or False
print(x)
type(x)


x=(True or True) and (not False and True)
print(x)
type(x)


x=(3>89) or (34>32) 
print(x)
type(x)


x= not True  and False
print(x)
type(x)
#question 4
x=int (input ("enter number")) 
if x%2==0 and x%5==0:
    print ("Hurray it is what I am looking for")
else: 
        print ("wrong number")

#question 5
x=int (input ("enter number"))
if x>10 and x<50:
    print ("yes I am in range")
else:
    print("oops")
#question 6
#Ladder if
brand=input("Enter your favorite brand")
if brand=='RC':
    print('it is children brand')
    
elif brand=='KF':
    print('it is not that much kick')
elif brand=='FO':
    print('buy one get one free')
        
else:
     print('other brands are not recommended')

#nested if
i = 10
if (i == 10): 
    if (i < 15): 
        print ("i is smaller than 15") 
    
    if (i < 12): 
        print ("i is smaller than 12 too") 
    else: 
        print ("i is greater than 15")
 



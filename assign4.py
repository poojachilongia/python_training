import math
import random 
print("banking operation")
OTP=1234
   
user=int(input("enter OTP"))
while user!=OTP:
    k=0
    print("sorry i didn't understand")
    
    user=int(input("enter correct OTP"))
    k=k+1
       
print("what u wanna do!!!")



userdata={}
transaction=input("\n1.new account\n2.withdraw\n3.deposit\n4.balance enquiry\n5.demand draft\n6.cancel\nchoose option")

if transaction=="new account":
    print("enter details")
    name=input("enter your name")
    age=int(input("enter your age"))
    address=input("enter adress:")
    phone=int(input("enter phone no." ))
    gender=input("gender")

    userdata["name"]=name
    userdata["age"]= age
    userdata["address"]= age 
    userdata["phone"]= age          
    userdata["gender"]= age
    print("ACCOUNT CREATED")
elif transaction=="withdraw":
    amount=int(input("enter the amount you want to withdraw"))
    balance=random.randint(1,5000)
    print(balance)
    if amount>=100 and amount<10000:
        balance=balance-amount
        print("here is your money")
        print("balance is :",balance)
    else:
         print("the amount should be in range 100 and 10000")
elif transaction=="deposit":
    amount=int(input("enter the amount you want to deposit"))
    bal=random.randint(1,10000)
    print("your current balance is:",bal)
    if amount**5:
        print("amount is deposited")
        bal=bal+amount
        print("your new balance is")
        print(bal)
    else:
        print("enter the correct amount")
elif transaction=="balance enquiry":
    print("enter any one of the following")
    a=input("\n1.deposit amount\n2.outstanding balance\n3.minimum Due amount")
    if a=="deposit amount":
        print("your deposit amount is: ",random.randint(1,100000))
    elif a=="outstanding balance":
            print("your outstanding balance is " ,random.randint(1,500))
    elif a=="minimum amount due":
            print("your minimum due is",random.randint(1,500))
elif transaction=="Demand Draft":
    print("enter following details")
    bank_name=input("name of the bank")
    accountholder=input("name of account holder")
    branch=input("name of branch")
    amount=int(input("enter amount"))
elif transaction=="cancel":
            print("thank you") 
   
  
      
else:
        print("enter the correct value")
    
   

          


    



import random
firstname=str(input('enter first name'))
lastname=str(input('enter 2nd name'))
def generateOTP():
    OTP=int(input("enter the number"))
    
    if OTP>21:
        print("the number entered is wrong try again")
    
    OTP1=random.randint(1,21)
    print("your one time password is")
    print(OTP1)
    if OTP==OTP1:
        print("your OTP matched successfully")
    else:
        print("ERROR!!! enter the OTP again")
        return OTP
   
generateOTP()
for x in range(3):
     print("would you like to give another chance if yes(y) if no(n)")
     try_again=input("enter the choice")
     if try_again=="y":
         generateOTP()
     else:
         print(" thanks for attempt")
         break
     print(" sorry program crashed")

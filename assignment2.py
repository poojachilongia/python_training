#question 1
x=[1,2,3,4,[10,20,30,40,[100,200,300,400],"riyazulhaque",5+5j],4000]
print (x[4][0:2])
print(x[4][6])
print(x[4][4][2:4])
print(x[4][3:6])

#question 2
import random
deck=list(range(1,21))
hand=random.sample(deck,2)
if sum(hand)%2==0:
    print(hand)

#question 3
y="hello&*$$world"
letter=dict()
for i in y:
    if i not in letter:
        letter[i]=1
    
    else:
        letter[i]=letter[i]+1
print(letter)
print(letter.get("*"))
print(letter.get("$"))

#question 4
for x in range(1,50):
    if (x%2!=0):
        print(x**3)

#question 5
my_list=[10,20,40,90,100]
my_new_list=[]
for i in my_list:
    my_new_list.append(i*5)

print(my_new_list)
print(my_list)
#question 6
s="hello  world i am learning python"
words=s.split()
letter={w:len(w) for w in words}
print(letter)

#question 7
items=[10,20,30,40,50,60,'winter','summer','spring']
if all(isinstance(i,int) for i in items):
     print("true")
else:
    print("false")



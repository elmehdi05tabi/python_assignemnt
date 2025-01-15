import random 
print (f"random number between 10 and 50 => {random.randint(10,50)}")
num1 =  random.randint(2,10)
num2 =  random.randint(1,9)
if num1%2==0 :  
    print (f"random number between 2 and 10 => {num1}")
else : 
    print (f"random number between 2 and 10 => {num1+1}")
if num2%2!=0 :  
    print (f"random number between 2 and 10 => {num2}")
else : 
    print (f"Random Odd Number Between 1 And 9 => {num2-1}")
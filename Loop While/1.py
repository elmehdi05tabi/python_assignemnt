# Input
num = 0

# Needed Output
"Number 0 Is Not Larger Than 0"
# Input
num = 10

# Needed Output
9
8
7
5
4
3
2
1
"8 Numbers Printed Successfully."
num=int(input("select the number "))
c=0
if num > 0 :
   num-=1
   while num > 0 :
    if num != 6:
      print(num) 
      c+=1
    num-=1
   else:
      print(f"{c} Numbers Printed Successfully. ")

else :
    print(f"Number {num} Is Not Larger Than 0")
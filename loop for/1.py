# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]

# Needed Output
"1 => 20"
"2 => 15"
"3 => 5"
"All Numbers Printed"
a = 0
for number in my_nums :
    if number % 5 == 0 :
        a+=1
        print(f"{a} => {number}")
values = (0, 1, 2)

if any(values): # this is true because we have the value true in tuple 

  my_var = 0 

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
#  is true because the i have the value true in firs 4 value i don't now for autre value because i have one true 
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):  

  print("Good")

else:

  print("Bad")
# this code print "good"
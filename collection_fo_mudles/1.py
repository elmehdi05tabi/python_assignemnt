my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []
final_string = ""
for data in zip(my_list, my_tuple):
       for i in data : 
        final_string += i 
              

print(final_string) # Elzero
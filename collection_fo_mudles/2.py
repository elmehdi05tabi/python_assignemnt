my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []
final_string = ""
for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    my_data.append(item1)
for i in  range(len(my_data)-2) : 
        final_string += my_data[i] 

print(final_string)
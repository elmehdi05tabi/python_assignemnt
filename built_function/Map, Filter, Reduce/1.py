def remove_chars (name):
    # ch=""
    # for i in range(1,len(name)-1):
    #     ch += name[i] 
    return name[1:-1]
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list = map(remove_chars , friends_map)
for name in cleaned_list : 
    print(name)
print("="*50) 
#  Type 2 : 
cleaned_list = map(lambda name :name[1:-1], friends_map)
for name in cleaned_list : 
    print (name)
def  get_names(name) : 
        return name.endswith("m") 
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names = filter (get_names,friends_filter) 
for name in names : 
    print(name)
print("="*50)
# With lambda : 
names = filter (lambda name :name.endswith("m") ,friends_filter) 
for name in names : 
    print(name)
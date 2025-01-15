# Input
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

# Needed Output
"Mohamed"
"Shady"
"Sherif"
"Friends Printed And Ignored Names Count Is 2"

c = 0 
a = 0 
while a< len(friends):
    if friends[a]==friends[a].capitalize() :
        print(friends[a])
    else : 
        c+=1 
    a+=1
print(f"Friends Printed And Ignored Names Count Is {c}")

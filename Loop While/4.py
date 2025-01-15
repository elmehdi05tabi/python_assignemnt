friends = [] 
a = 4
while a > 0 :
    b = input("entre name of friends ")
    if b == b.upper() : 
        print("name note valide")
    elif b == b.lower():
        friends.append(b)
        friends.append(b.capitalize())
        print(f"your name{b}now is name capitalize")
        print(f"Names Left in List Is {a-1}")
        a-=1
    else : 
        friends.append(b)
        print(f"Friend {b} Added")
        print(f"Names Left in List Is {a-1}")
        a-=1
    print(friends)
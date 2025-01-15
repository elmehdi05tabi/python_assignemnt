NUM =input("Add Your Number ")
if len(NUM) > 1 : 
    raise IndexError("IndexError: Only One Character Allowed")
elif 1<=(int(NUM))<= 9: 
    print(f"The Number Is {NUM}")
elif int(NUM) == 0 : 
    raise ValueError (f"ValueError: Number Must Be Larger Than {NUM}")
elif type(NUM) == str : 
    raise Exception ("Exception: Only Numbers Allowed") 
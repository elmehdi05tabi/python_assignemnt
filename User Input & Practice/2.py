# Inputs

16 # Input One
24 # Input Two

# Needed Output

"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
"Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+

age=int(input("don your age please :").strip(" "))
if age < 16 :
    print(f"Hello Your Age Is Under {age}, Some Articles Is Not Suitable For You")
else: 
        print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
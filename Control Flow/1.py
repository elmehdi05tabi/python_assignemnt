# Inputs

num1 = int(input("entre  the numbre:"))
num2 = int(input("entre  the numbre:"))
operation = input("""select operation "+" Or "-" Or "*" Or "/" Or "%" """).strip()

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800

if operation == "+":
    print(f"{num1}+{num2}={num1 + num2}")
elif operation == "-" :
     print(f"{num1}-{num2}={num1 - num2}")
elif operation == "*" :
     print(f"{num1}*{num2}={num1 * num2}")
elif operation == "/" :
     print(f"{num1}/{num2}={num1 / num2}")
elif operation == "%" :
     print(f"{num1}%{num2}={num1 % num2}")
         
                 
        
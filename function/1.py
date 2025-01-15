def calculate(a,b,calc):
    add = a+b 
    substarct = a-b
    multiply = a/b
    if calc == "add" or calc =="a"  :
       return add 
    elif calc == "sub" or calc =="s" :
        return substarct
    elif calc == "mul" or calc=="m" :
        return multiply
    
c = input("entre the type of the calculate :").lower()
a = int(input("entre the firs number:"))
b = int(input("entre the second number:"))
print(calculate(a,b,c))
def my_all (test) :
    good  = True
    for testing in test : 
        if bool(testing)== False : 
            good = False 
    if good == True :
        return "True"
    else : 
        return "False"
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False
#   2 
def my_any (test) :
    good  = False
    for testing in test : 
        if bool(testing)== True : 
            good = True 
    if good == True :
        return "True"
    else : 
        return "False"
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False
#  3 
def my_min(ls) :
    min = ls[0]
    for i in range(len(ls)) :
        if ls[i] < min : 
            min = ls[i]
    return min
        
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100
# 4

def my_max(ls) :
    max = ls[0]
    for i in range(len(ls)) :
        if ls[i] > max : 
            max = ls[i]
    return max
        
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700
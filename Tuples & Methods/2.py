friends = ("Osama", "Ahmed", "Sayed")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements
x= list(friends)
x[0]="elzero"
print(tuple(x))
print(type(friends))
y=len(friends)
print(f"{y} elment")
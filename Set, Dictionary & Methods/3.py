my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3}
# set()
# {"A", "B"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("a")
my_set.add("b")
print(my_set)
letters.remove("C")
letters.discard("K")
print(letters)
# Inputs

"Osama" # First Name
"Mohamed" # Second Name

# Needed Output

"Hello {First_Name} {First_Letter_From_Second_Name}." # Example "Osama M."
first_name  =input("entre your first name please :").strip(" ").capitalize()
second_name =input("entre your seconde name please :").strip(" ").capitalize()
print(f"hello {first_name} {second_name:.1s}")

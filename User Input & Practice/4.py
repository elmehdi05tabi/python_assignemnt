# Inputs

"Osama@Nn.Sa" # Email

# Needed Output

"Your Name Is Osama"
"Email Service Provider Is nn"
"Top Level Domain Is sa"
email=input("entre your email :")
a = email[:email.index("@")] 
b = email[email.index("@")+1:email.index(".")] 
c =  email[email.index(".")+1:] 
print(f"your name is {a} ")
print(f"your services provider  is {b} ")
print(f"your level demaine  is {c} ")
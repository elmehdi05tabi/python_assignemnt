# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country")
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

# Needed Output
"Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
"Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example
if country in countries : 
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
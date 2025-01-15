# Create Your Decorator Here
def decor (func)  :
  def decorn() :
    print("Sugar Added From Decorators")
    func()
    print("#"*20)
  return decorn

@decor
def make_tea():
  print("Tea Created")
@decor
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()

# Needed Output

"Sugar Added From Decorators"
"Tea Created"
"####################"
"Sugar Added From Decorators"
"Coffe Created"
"####################"
class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C:

  def __init__(self, three):

    self.three = three
class Name(A,B,C) : 
  def __init__(self,one,two,three) : 
    A.__init__(self,one)
    B.__init__(self,two)
    C.__init__(self,three)
  def  show_name(self) :
    return self.one + self.two + self.three
class Text (Name) : 
  def  show_name(self) :
    return f"The Name is {self.one + self.two + self.three}"
the_name = Text("El", "ze", "ro")
print(the_name.show_name())

# Ouput
# The Name Is Elzero
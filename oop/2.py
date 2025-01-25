class User:
 def __init__ (self,fname,lname,age,sex) :
    self.fname =fname
    self.lname =lname
    self.age =age 
    self.sex =sex
 def full_details (self) : 
   age = 40 - self.age
   if self.sex == "Male" : 
     return f" Hello Mr {self.fname} {self.lname:.1s} [{str(age).zfill(2)}]  Years to Reach 40 "
   elif self.sex == "Female" : 
     return f" Hello Mrs {self.fname} {self.lname:.1s} [{str(age).zfill(2)}]   Years to Reach 40 "
     

user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40
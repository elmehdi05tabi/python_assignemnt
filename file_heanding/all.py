for i in range(1,51) :
  file = open(rf"C:\Python2\txt{i}.txt","w")
  if i != 25 : 
     file.write(f"Elzero Web School => {i}")
import os 
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))
print(len(os.path.dirname(os.path.abspath(__file__))))

# 2 
file = open(r"C:\Python2\txt1.txt","r")
print(file.read())
file = open(r"C:\Python2\txt1.txt","a")
file.write("\nAppended => Elzero Web School"*50)
# 3 
c=0
file = open(r"C:\Python2\txt1.txt","r") 
for i in file : 
   c+=1
print(f"the number of line is => {c}")
file = open(r"C:\Python2\txt1.txt","r") 
word = file.read()
word.split()
print(len(word))

#  4 

for i in file:
   import os 
   if file.
   os.remove(file)

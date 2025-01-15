def addition(*a) :
  s = 0 
  for i in a :
    
    if i == 10 :
      continue 
    if i == 5 :
      s -= 10 
    s+= i
  return s 

print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160
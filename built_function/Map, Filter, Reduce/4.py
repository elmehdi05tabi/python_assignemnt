skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for counter , skill in enumerate(reversed(list(skills)),50) : 
         if skill == 10 or skill == 20 :
          continue
         print(f"{counter}-{skill}")
        
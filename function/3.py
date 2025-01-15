def show_skills(name ,*skills) :
   if len(skills) == 0 :  # this for calculate the nombre and show if a have the the value in the skills  
      print(f"hello {name} you have not skills to show ")
   else :
      print(f"hello {name} your skills is")
   for skill_value in skills : 
       print(f"-{skill_value}")
show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")

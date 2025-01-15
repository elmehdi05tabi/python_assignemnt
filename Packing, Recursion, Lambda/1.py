def get_score(**dicte):
    for key,val in dicte.items():
        print(f"{key}=>{val}")
         
    
get_score(Math=90, Science=80, Language=70) 
print("="*40)
get_score(Logic=70, Problems=60)
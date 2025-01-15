def get_people_scores (*name,**score):
    for i in name :
       if len(score) !=0: 
         print(f"hello {i} this is your score table :")
       else :
         print(f"hello {i} you dont have anny score ")
    # if name==False:
    #    print("")
    for key,val in score.items() :
        print(f"{key}=> {val}")
# test 1 :
get_people_scores("elmehdi",franch=90,english=50,python=70)
print("="*50)
# test 2 :
get_people_scores("tabi",foot=100,basket=0)
print("="*50)
# test 3 :
get_people_scores(Logic=70, Problems=60)
print("="*50)
# test 3 :
get_people_scores("elmehdi")
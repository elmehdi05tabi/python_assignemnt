scr = {
    "math" : 90,
    "science" : 80,
    "language" :70
}
def get_the_scores(*name,**scores):
    for i in name :
      if len(scores)!=0:
        print(f"hello {i} this is your score table : ")
      else :
         print(f"hello{i} you have note score to show")     
    for key,val in scores.items() :
        print(f"{key} => {val}")
# test 1
get_the_scores("elmehdi", **scr)
print("="*50)
# test 2
get_the_scores("elmehdi")
print("="*50)
# test 3 
get_the_scores(**scr)
class Games:
   def __init__(self,list_game):
     self.list_game = list_game 
   def show_games(self) :
      if type(self.list_game) == str : 
         print(f"I Have One Game Called {self.list_game}")
      elif type(self.list_game) == int : 
         print(f"I Have {self.list_game} Game.")
      elif type(self.list_game) == list : 
         print(" I Have Many Games:")
         for i in self.list_game : 
            print(f"- {i}")
my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# # Ouput
# # I Have Many Games:
# # -- Ys II
# # -- Ys Oath In Felghana
# # -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.
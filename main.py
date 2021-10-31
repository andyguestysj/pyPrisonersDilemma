from player import Player
from strategies import StratAlwaysCooperate, StratAlwaysDefect, StratTitForTat, StratRandom

player1 = Player()
player2 = Player()

player1.setStrategy(StratRandom())
player2.setStrategy(StratTitForTat())
p1_score=0
p2_score=0

history = []

# Prisoners can Cooperate "C" or Defect "D"

VERBOSE = False

print("START")

for i in range(10):  
  p1_choice = player1.playMove(history,1)
  p2_choice = player2.playMove(history,2)
  
  if VERBOSE:
    print("P1 chose ",p1_choice," P2 chose ",p2_choice)

  if p1_choice == p2_choice == "D":
    if VERBOSE:
      print("Both defect")
    p1_score = p1_score + 1
    p2_score = p2_score + 1
  elif p1_choice == p2_choice == "C":
    if VERBOSE:
      print("Both cooperate")
    p1_score = p1_score + 3
    p2_score = p2_score + 3
  elif p1_choice == "D" and p2_choice == "C":
    if VERBOSE:
      print("P1 betrays P2")
    p1_score = p1_score + 5
  elif p1_choice == "C" and p2_choice == "D":
    if VERBOSE:
      print("P2 betrays P1")
    p2_score = p2_score + 5

  history.append([p1_choice, p2_choice])  

print("Final scores : P1 ", p1_score, " P2 ", p2_score)

print("END") 
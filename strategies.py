import abc
import random

class PlayStrat(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def playMove(self,game_history,player_no): 
    """Required Method"""

class StratAlwaysCooperate(PlayStrat):
  def playMove(self,game_history,player_no): 
    # Cooperate    
    return "C";

class StratAlwaysDefect(PlayStrat):
  def playMove(self,game_history,player_no): 
    # Defect
    return "D";

class StratRandom(PlayStrat):
  def playMove(self,game_history,player_no): 
    if random.randint(0, 1)==0:
      return "C"
    else:
      return "D"

class StratTitForTat(PlayStrat):
  def playMove(self,game_history,player_no): 
    if player_no==1:
      other_player = 1
    else:
      other_player = 0
    # Cooperate   
    if len(game_history)==0:
      return "C";
    else:       
      return game_history[len(game_history)-1][other_player];
    #return "D";

# Prisoners can Cooperate "C" or Defect "D"
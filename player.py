class Player():
  def  __init__(self):
    pass
  def setStrategy(self, myStrategy):
    self.play = myStrategy  
  def playMove(self,game_history,player_no):
    return self.play.playMove(game_history,player_no)

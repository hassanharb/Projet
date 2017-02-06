from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation, SoccerAction
from toolbox import MyState, Action
from soccersimulator import Vector2D
from soccersimulator.settings import *

def fonceur(mystate):
    return SoccerAction(mystate.ball_position-mystate.my_position,mystate.position_but_adv-mystate.my_position)

   
## Strategie
class ElLooser(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        return SoccerAction(Vector2D(0,0),mystate.position_but_adv)



class ElStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        return fonceur(mystate)
 


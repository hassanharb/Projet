from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation, SoccerAction
from soccersimulator import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D
from soccersimulator.settings import *
from toolbox import MyState, Action
from strat import fonceur, defonceur


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
 


class ElDefenseur(Strategy):
    def __init__(self):
       Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        return defonceur(mystate)







#    mystate = MyState(state,id_team,id_player)
#    mystate.middle
 
 #       if Vector2D(75,45).distance(state.player_state(id_team,id_player).position)>0.3 :
 #           return SoccerAction(Vector2D(75,45)-state.player_state(id_team,id_player).position,Vector2D())









## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Hassan",ElDefenseur())
team1.add("Booba",ElLooser())
team2.add("Paul",ElStrategy())
team2.add("Pogba",ElLooser())




#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
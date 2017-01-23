from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation, SoccerAction
from soccersimulator import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D
from soccersimulator.settings import *
from toolbox import MyState


## Strategie aleatoire
class ElAttaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),Vector2D(mystate.position_but_adv()))


#class ElDefenseur(Strategy):
#    def __init__(self):
 #       Strategy.__init__(self,"Random")position_but_adv
 #   def compute_strategy(self,state,id_team,id_player):
#        return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),Vector2D(1,1))








#    mystate = MyState(state,id_team,id_player)
#    mystate.middle
 
 #       if Vector2D(75,45).distance(state.player_state(id_team,id_player).position)>0.3 :
 #           return SoccerAction(Vector2D(75,45)-state.player_state(id_team,id_player).position,Vector2D())









## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Hassan",ElStrategy())
team1.add("Booba",ElStrategy())
team2.add("Paul",ElStrategy())
team2.add("Pogba",ElStrategy())
 





#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
from toolbox2 import MyState, Action
from soccersimulator.settings import *

GOLF = 0.001
SLALOM = 10.

        
class GolfStrat(Strategy):
    def __init__(self):
        super(GolfStrat,self).__init__("Golf")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action=Action(mystate)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return action.shoot_but_adv
            
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
#        if(mystate.ball_position.y==GAME_HEIGHT/2):
        if mystate.dist_ball(zone.position+Vector2D(zone.l/2.,zone.l/2.))>20:
            return action.shoot(zone.position+Vector2D(zone.l/2.,zone.l/2.))
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return SoccerAction()
        """ sinon """
#        distance = state.player_state(id_team,id_player).position.distance(zone.position+zone.l/2.)
        return action.mini_shoot(zone.position+Vector2D(zone.l/2.,zone.l/2.))
        


class SlalomStrat(Strategy):
    def __init__(self):
        super(SlalomStrat,self).__init__("Slalom")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action=Action(mystate)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return action.shoot_but_adv
            
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        return action.mini_shoot2(zone.position+Vector2D(zone.l/2.,zone.l/2.))
    
    
team1 = SoccerTeam()
team2 = SoccerTeam()
team1.add("John",GolfStrat())
team2.add("John",SlalomStrat())
simu = Parcours1(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours2(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours3(team1=team1,vitesse=SLALOM)
show_simu(simu)
simu = Parcours4(team1=team1,team2=team2,vitesse=SLALOM)
show_simu(simu)

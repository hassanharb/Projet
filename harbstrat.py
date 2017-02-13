from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation, SoccerAction
from toolbox import MyState, Action
from soccersimulator import Vector2D
from soccersimulator.settings import *


def fonceurball(mystate):
    return SoccerAction((mystate.ball_position-mystate.my_position)+(mystate.ball_vitesse)*10,Vector2D())
    
def fonceur_mini(mystate):
    return SoccerAction((mystate.ball_position-mystate.my_position)+(mystate.ball_vitesse)*10,(mystate.position_but_adv-mystate.my_position).norm_max(1.5))
    
def fonceur(mystate):
    return SoccerAction((mystate.ball_position-mystate.my_position),mystate.position_but_adv-mystate.my_position)

        
def donothing():
    return(SoccerAction(Vector2D(0,0),Vector2D(0,0)))

def ralentir_peu(mystate,action):
        return SoccerAction((mystate.ball_position-mystate.my_position).norm_max(0.1),Vector2D())
def ralentir_moyen(mystate,action):
        return SoccerAction((mystate.ball_position-mystate.my_position).norm_max(0.05),Vector2D())
def ralentir_bcp(mystate,action):
        return SoccerAction((mystate.ball_position-mystate.my_position).norm_max(0.01),Vector2D())

def defonceur(mystate,action):
    if(mystate.my_position.distance(mystate.ball_position)<1.65):
        #return(action.shoot_but_adv)
        return SoccerAction(mystate.ball_position-mystate.my_position,mystate.position_but_adv-mystate.joueurplusProche)
        
    if mystate.my_position.distance(mystate.ball_position)<5:
        return ralentir_peu(mystate,action)
    if(mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH/2):
        return fonceurball(mystate)
    if(mystate.position_mon_but.x==GAME_WIDTH):
        return action.sprint(Vector2D(4*GAME_WIDTH/5,mystate.ball_position.y))
    else:
        return action.sprint(Vector2D(GAME_WIDTH/5,mystate.ball_position.y))

class ElDefenseur(Strategy):
    def __init__(self):
       Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action=Action(mystate)
        return defonceur2(mystate,action)


class Bestdeftest(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action=Action(mystate)
        return defonceur2(mystate,action)
        




## [ (idt,idp) for idt,idp in self.state.players if idt== self.idt and idp != self.idp]
## Strategie
class ElLooser(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Brute")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        return donothing()



class ElStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"ElMatador")
        self.mydic = dict()
        self.mydic["c"] = 0
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action= Action(mystate)
        self.mydic["c"]+=1
        if self.mydic["c"]<0:
            return donothing()
        if mystate.my_position.distance(mystate.ball_position)<1.65:
            return(action.shoot_but_adv)
        if mystate.my_position.distance(mystate.ball_position)<3:
            return ralentir_bcp(mystate,action)
        if mystate.my_position.distance(mystate.ball_position)<7:
            return ralentir_moyen(mystate,action)
        if mystate.my_position.distance(mystate.ball_position)<9:
            return ralentir_peu(mystate,action)
        if mystate.my_position.distance(mystate.ball_position)<10 :
            return fonceurball(mystate)
        if mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH/2 :
            if mystate.my_position.distance(mystate.milieu_terrain - mystate.my_position + (mystate.position_but_adv-mystate.milieu_terrain)/2)<10:
                return ralentir(mystate,action)
            return action.sprint(mystate.milieu_terrain + (mystate.position_but_adv-mystate.milieu_terrain)/9)
        return fonceurball(mystate)


class ElStrategySolo(Strategy):
    def __init__(self):
        Strategy.__init__(self,"ElMatadorSolo")
        self.mydic = dict()
        self.mydic["c"] = 0
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action= Action(mystate)
        self.mydic["c"]+=1
        if self.mydic["c"]<0:
            return donothing()
 
 
#        if(mystate.position_mon_but.x==0): 
#            if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.6):
#                return fonceur_mini(mystate)
                
        if(mystate.position_mon_but.x==GAME_WIDTH):        
            if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.6):
                return fonceur_mini(mystate)
                
#        if(mystate.position_mon_but.x==0):        
#            if (mystate.position_mon_but.distance(mystate.ball_position)>GAME_WIDTH*0.6):
#                return fonceurball(mystate)
                
        if(mystate.position_mon_but.x==GAME_WIDTH):        
            if (mystate.position_mon_but.distance(mystate.ball_position)>=GAME_WIDTH*0.6):
            
                return fonceurball(mystate)

        if mystate.my_position.distance(mystate.ball_position)<1.65:
            return fonceurball(mystate)
#        if mystate.my_position.distance(mystate.ball_position)<3:
#            return ralentir_bcp(mystate,action)
        if mystate.my_position.distance(mystate.ball_position)<9:
            return ralentir_moyen(mystate,action)
        if mystate.my_position.distance(mystate.ball_position)<11:
            return ralentir_peu(mystate,action)
            
        if (mystate.position_mon_but.distance(mystate.ball_position)<=GAME_WIDTH/2):
            if(mystate.position_mon_but.x==GAME_WIDTH or mystate.position_mon_but.x==0):
                return action.sprint(Vector2D(0.5*GAME_WIDTH,mystate.ball_position.y))
                
        if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.65):
            if(mystate.position_mon_but.x==GAME_WIDTH):
                return action.sprint(Vector2D(0.65*GAME_WIDTH,mystate.ball_position.y))
        if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.45):
            if(mystate.position_mon_but.x==0):
                return action.sprint(Vector2D(0.45*GAME_WIDTH,mystate.ball_position.y))
                
#        if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.65):
#            if(mystate.position_mon_but.x==GAME_WIDTH or mystate.position_mon_but.x==0):
#             return fonceurball(mystate)           
          
        if (mystate.my_position.distance(mystate.ball_position)<5):
            return fonceurball(mystate)
        return fonceurball(mystate)


class ElDefenseur(Strategy):
    def __init__(self):
       Strategy.__init__(self,"ElMonstro")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action= Action(mystate)
        return defonceur(mystate,action)








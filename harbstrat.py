from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation, SoccerAction
from toolbox import MyState, Action
from soccersimulator import Vector2D
from soccersimulator.settings import *
import random


def fonceurball(mystate):
    return SoccerAction((mystate.ball_position-mystate.my_position)+(mystate.ball_vitesse)*10,Vector2D())
    
def fonceurballdef(mystate):
    return SoccerAction(mystate.ball_position-mystate.my_position+(mystate.ball_vitesse)*5,Vector2D())
    
def fonceur_mini(mystate):
    return SoccerAction((mystate.ball_position-mystate.my_position)+(mystate.ball_vitesse)*10,(mystate.position_but_adv-mystate.my_position).norm_max(1.0))
    
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
        return action.petit_shoot_joueur_proche
    
    if(mystate.my_position.distance(mystate.ball_position)<7):
        return fonceurballdef(mystate)
        
    p=SoccerAction((mystate.position_mon_but-mystate.my_position)+(mystate.ball_position-mystate.position_mon_but)/2,Vector2D()) 
    
    if(mystate.position_mon_but.distance(mystate.ball_position)>GAME_WIDTH*0.39 and mystate.my_position.distance(mystate.ball_position)>mystate.joueurAdv_plusProche.distance(mystate.ball_position)):
        return p
              
    if(mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH/2):
        return fonceurball(mystate)
        
    
    if(mystate.my_position.distance((mystate.position_mon_but-mystate.my_position)+(mystate.ball_position-mystate.position_mon_but)/2)<6):
        return donothing()
    return p
    
def defonceur4(mystate,action):
    
    if(mystate.my_position.distance(mystate.ball_position)<1.65):
        return action.petit_shoot_joueur_proche
    
    if(mystate.my_position.distance(mystate.ball_position)<7):
        return fonceurballdef(mystate)
        
    p=SoccerAction((mystate.position_mon_but-mystate.my_position)+(mystate.ball_position-mystate.position_mon_but)/2,Vector2D())
    pp=SoccerAction((mystate.position_mon_but-mystate.my_position)+(mystate.ball_position-mystate.position_mon_but)/1.75,Vector2D())
    
    
    if mystate.ball_position.distance(Vector2D(mystate.ball_position.x,GAME_HEIGHT))<GAME_HEIGHT*0.25 or mystate.ball_position.distance(Vector2D(mystate.ball_position.x,GAME_HEIGHT))>GAME_HEIGHT*0.75:
        return pp
        
        
    if(mystate.position_mon_but.distance(mystate.ball_position)>GAME_WIDTH*0.42 and mystate.my_position.distance(mystate.ball_position)>mystate.joueurAdv_plusProche.distance(mystate.ball_position)):
        return p
              
    if(mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH/2):
        return fonceurball(mystate)
        
    
    if(mystate.my_position.distance((mystate.position_mon_but-mystate.my_position)+(mystate.ball_position-mystate.position_mon_but)/2)<6):
        return donothing()
    return p


def ailierGauche(mystate,action):
    
    if(mystate.my_position.distance(mystate.ball_position)<1.65 and mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.5):
                return action.petit_shoot_but_adv
                
    if(mystate.my_position.distance(mystate.ball_position)<1.65 and mystate.position_mon_but.distance(mystate.ball_position)<0.62*GAME_WIDTH and mystate.position_mon_but.distance(mystate.ball_position)>0.5*GAME_WIDTH):
         rand=random.randint(0,3)
         print(rand)
         if(rand==0):
            return action.petit_shoot_ailier_joueur_proche
         else:
            return action.petit_shoot_but_adv
        
        
    if(mystate.my_position.distance(mystate.ball_position)<1.65 and mystate.position_mon_but.distance(mystate.ball_position)>=0.65*GAME_WIDTH):
        return action.shoot_but_adv

    if mystate.my_position.distance(mystate.ball_position)<10:
            return fonceurballdef(mystate)            
                
    if(mystate.position_mon_but.x==0):
        if mystate.ball_position.distance(Vector2D(mystate.ball_position.x,GAME_HEIGHT))<GAME_HEIGHT*0.35:
            return fonceurball(mystate)
        
            
        if(mystate.position_mon_but.distance(mystate.ball_position)>GAME_WIDTH/2):
            return action.sprint(Vector2D(GAME_WIDTH*0.6,GAME_HEIGHT*0.7))
            
        return action.sprint(Vector2D(GAME_WIDTH*0.35,GAME_HEIGHT*0.7))
        
    if(mystate.position_mon_but.x==GAME_WIDTH):
        if mystate.ball_position.distance(Vector2D(mystate.ball_position.x,GAME_HEIGHT))>GAME_HEIGHT*0.65:
            return fonceurball(mystate)
            
        if(mystate.position_mon_but.distance(mystate.ball_position)>GAME_WIDTH/2):
            return action.sprint(Vector2D(GAME_WIDTH*0.4,GAME_HEIGHT*0.3))
        return action.sprint(Vector2D(GAME_WIDTH*0.65,GAME_HEIGHT*0.3))
        
    return fonceurball(mystate)
        
        
def ailierDroit(mystate,action):
    
    if(mystate.my_position.distance(mystate.ball_position)<1.65 and mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.5):
                return action.petit_shoot_but_adv
                
    if(mystate.my_position.distance(mystate.ball_position)<1.65 and mystate.position_mon_but.distance(mystate.ball_position)<0.62*GAME_WIDTH and mystate.position_mon_but.distance(mystate.ball_position)>0.5*GAME_WIDTH):
        rand=random.randint(0,3)
        print(rand)
        if(rand==0):
            return action.petit_shoot_ailier_joueur_proche
        else:
            return action.petit_shoot_but_adv
        
    if(mystate.my_position.distance(mystate.ball_position)<1.65 and mystate.position_mon_but.distance(mystate.ball_position)>=0.65*GAME_WIDTH):
        return action.shoot_but_adv     
    
    if mystate.my_position.distance(mystate.ball_position)<10:
            return fonceurballdef(mystate)
        
    if(mystate.position_mon_but.x==0):
        if mystate.ball_position.distance(Vector2D(mystate.ball_position.x,GAME_HEIGHT))>GAME_HEIGHT*0.65:
            return fonceurball(mystate)
            
        if(mystate.position_mon_but.distance(mystate.ball_position)>GAME_WIDTH/2):
            return action.sprint(Vector2D(GAME_WIDTH*0.6,GAME_HEIGHT*0.3))
            
        return action.sprint(Vector2D(GAME_WIDTH*0.35,GAME_HEIGHT*0.3))
        
    if(mystate.position_mon_but.x==GAME_WIDTH):
        if mystate.ball_position.distance(Vector2D(mystate.ball_position.x,GAME_HEIGHT))<GAME_HEIGHT*0.35:
            return fonceurball(mystate)
            
        if(mystate.position_mon_but.distance(mystate.ball_position)>GAME_WIDTH/2):
            return action.sprint(Vector2D(GAME_WIDTH*0.4,GAME_HEIGHT*0.7))
            
        return action.sprint(Vector2D(GAME_WIDTH*0.65,GAME_HEIGHT*0.7))
        
    return fonceurball(mystate)
    
class ElAilierDroit(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Brute")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action=Action(mystate)
        return ailierDroit(mystate,action)
        
class ElAilierGauche(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Brute")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action=Action(mystate)
        return ailierGauche(mystate,action)
        
        
class ElDefenseur(Strategy):
    def __init__(self):
       Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action=Action(mystate)
        return defonceur(mystate,action)
        
class ElDefenseur4(Strategy):
    def __init__(self):
       Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action=Action(mystate)
        return defonceur(mystate,action)


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
        
class ElLooser2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Brute")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action=Action(mystate)
        return ailierDroit(mystate,action)



class ElStrategy(Strategy):
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
            
        if mystate.my_position.distance(mystate.ball_position)<1.65:
            if(mystate.position_mon_but.distance(mystate.ball_position)>GAME_WIDTH*0.35 and mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.65):
                return(action.petit_shoot_but_adv)
            return(action.shoot_but_adv)
            
        if mystate.my_position.distance(mystate.ball_position)<10:
            return fonceurballdef(mystate)
            
#        if mystate.my_position.distance(mystate.ball_position)<3:
#            return ralentir_bcp(mystate,action)
#        if mystate.my_position.distance(mystate.ball_position)<7:
#            return ralentir_moyen(mystate,action)
#        if mystate.my_position.distance(mystate.ball_position)<9:
#            return ralentir_peu(mystate,action)
#         
         
        if(mystate.position_mon_but.x==GAME_WIDTH):
            if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.25):
                return action.sprint(Vector2D(0.65*GAME_WIDTH,mystate.ball_position.y))
            if (mystate.position_mon_but.distance(mystate.ball_position)<=GAME_WIDTH/2): 
                return action.sprint(Vector2D(0.5*GAME_WIDTH,mystate.ball_position.y))
            
            
        if(mystate.position_mon_but.x==0):
            if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.45):
                return action.sprint(Vector2D(0.4*GAME_WIDTH,mystate.ball_position.y))

            if (mystate.position_mon_but.distance(mystate.ball_position)<=GAME_WIDTH/2):
                return action.sprint(Vector2D(0.5*GAME_WIDTH,mystate.ball_position.y))

        return fonceurball(mystate)
    
class ElAttaquant4(Strategy):
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
        p=SoccerAction((mystate.position_but_adv-mystate.my_position)+(mystate.ball_position-mystate.position_but_adv)/2,Vector2D())
        pp=SoccerAction((mystate.position_but_adv-mystate.my_position)+(mystate.ball_position-mystate.position_but_adv)/4,Vector2D())
        
        if mystate.my_position.distance(mystate.ball_position)<1.65:
            if(mystate.position_mon_but.distance(mystate.ball_position)>GAME_WIDTH*0.35 and mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.65):
                return(action.petit_shoot_but_adv)
            return(action.shoot_but_adv)
            
        if mystate.my_position.distance(mystate.ball_position)<7:
            return fonceurballdef(mystate)
            
        if (mystate.position_mon_but.distance(mystate.ball_position)>GAME_WIDTH/2):     
            if mystate.ball_position.distance(Vector2D(mystate.ball_position.x,GAME_HEIGHT))<GAME_HEIGHT*0.25 or mystate.ball_position.distance(Vector2D(mystate.ball_position.x,GAME_HEIGHT))>GAME_HEIGHT*0.75:
                return p
            if(mystate.my_position.distance(mystate.ball_position)>mystate.joueurplusProche.distance(mystate.ball_position)):
                return pp
#                return action.sprint(Vector2D(mystate.ball_position.x,GAME_HEIGHT/2))
            
         
        if(mystate.position_mon_but.x==GAME_WIDTH):
#            if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.25):
#                return action.sprint(Vector2D(0.65*GAME_WIDTH,mystate.ball_position.y))
            if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH/2): 
#                return p
                return action.sprint(Vector2D(0.4*GAME_WIDTH,mystate.ball_position.y))
            
            
        if(mystate.position_mon_but.x==0):
#            if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.45):
#                return action.sprint(Vector2D(0.4*GAME_WIDTH,mystate.ball_position.y))

            if (mystate.position_mon_but.distance(mystate.ball_position)<=GAME_WIDTH/2):
                 
#                return p
                return action.sprint(Vector2D(0.6*GAME_WIDTH,mystate.ball_position.y))

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
        if mystate.my_position.distance(mystate.ball_position)<1.65:
            return(action.shoot_but_adv)
#        if mystate.my_position.distance(mystate.ball_position)<3:
#            return ralentir_bcp(mystate,action)
#        if mystate.my_position.distance(mystate.ball_position)<7:
#            return ralentir_moyen(mystate,action)
#        if mystate.my_position.distance(mystate.ball_position)<9:
#            return ralentir_peu(mystate,action)
        return fonceurball(mystate)
#  









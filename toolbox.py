from soccersimulator import SoccerTeam, Simulation, SoccerAction
from soccersimulator import Vector2D
from soccersimulator.settings import *

class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.key = (idteam,idplayer)
        self.middle= Vector2D()
    @property
    def my_position(self):
        return self.state.player_state(self.key[0],self.key[1]).position
        #equivalent a self.player_state(self.key[0],self.key[1])
    @property    
    def ball_position(self):
        return self.state.ball.position
    @property    
    def milieu_terrain(self):
        return Vector2D(GAME_WIDTH/2,GAME_HEIGHT/2)
    @property    
    def ball_vitesse(self):
        return self.state.ball.vitesse
    @property
    def position_but_adv(self):
        if self.key[0]==1:
            return Vector2D(GAME_WIDTH,GAME_HEIGHT//2)
        else:
            return Vector2D(0,GAME_HEIGHT//2)
    @property
    def position_mon_but(self):
        if self.key[0]==1:
            return Vector2D(0,GAME_HEIGHT//2)
        else:
            return Vector2D(GAME_WIDTH,GAME_HEIGHT//2)

    def dist_player(self,p):
        return p.distance(self.my_position)
    @property
    def joueur_plus_proche(self):
        dmin=175
        for L in self.state.players :
            if L[0]==self.key[0] and L[1]!=self.key[1] and dmin>self.dist_player(state.player_state(L[0],L[1]).position) :
                dmin=self.dist_player(self.state.player_state(L[0],L[1]).position)
                player_proche=L
        return player_proche
    
    @property
    def joueurplusProche(self):
        dmin=0
        x=[(idt,idp) for idt,idp in self.state.players if idt == self.key[0] and idp != self.key[1]]
        dmin=x[0][1]
        
#        i=1
#        for i in x:
#            if(x[i]<dmin):
#                dmin=x[min]
        return self.state.player_state(x[0][0],x[0][1]).position
        
            
    
    
class Action(object):
    def __init__(self,mystate):
        self.state = mystate
    def sprint(self,p):
        return SoccerAction(p-self.state.my_position,self.state.middle)
    
    def shoot(self,p):
        return SoccerAction(self.state.middle,p-self.state.my_position)
    @property    
    def shoot_but_adv(self):
        return SoccerAction(Vector2D(0,0),self.state.position_but_adv-self.state.my_position)
    @property   
    def petit_shoot_but_adv(self):
        return SoccerAction(Vector2D(0,0),(self.state.position_but_adv-self.state.my_position).norm_max(2))
        
    @property
    def petit_shoot_joueur_proche(self):
        return SoccerAction(Vector2D(0,0),(self.state.joueurplusProche-self.state.my_position).norm_max(5.5))
    
    @property    
    def aller_vers_ball(self):
        return SoccerAction((self.state.ball_position-self.state.my_position,Vector2D(0,0)))
        

    
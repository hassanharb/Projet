from soccersimulator import SoccerTeam, Simulation, SoccerAction
from toolbox import MyState, Action
from soccersimulator import Vector2D
from soccersimulator.settings import *

def fonceur(mystate):
    return SoccerAction(mystate.ball_position-mystate.my_position,mystate.position_but_adv-mystate.my_position )

def defonceur(mystate):
    action=Action(mystate)
    if(mystate.positon_mon_but.distance(mystate.ball_position)<GAME_WIDTH//2):
        if(mystate.positon_mon_but.x==GAME_WIDTH):
            return action.sprint(Vector2D(3*GAME_WIDTH//4,GAME_HEIGHT//2))
        else:
            return action.sprint(Vector2D(GAME_WIDTH//4,GAME_HEIGHT//2))


def defonceur2(mystate,action):
    if(mystate.position_mon_but.distance(mystate.ball_position)<=GAME_WIDTH//4):
        return fonceur(mystate)

    if(mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH//2):
        if(mystate.position_mon_but.x==GAME_WIDTH):
            return action.sprint(Vector2D(3*GAME_WIDTH//4,mystate.ball_position.y))
        else:
            return action.sprint(Vector2D(GAME_WIDTH//4,mystate.ball_position.y))
    else:
        if(mystate.position_mon_but.x==GAME_WIDTH):
            return action.sprint(Vector2D(3*GAME_WIDTH//4,mystate.ball_position.y))
        else:
            return action.sprint(Vector2D(GAME_WIDTH//4,mystate.ball_position.y))
            


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
        

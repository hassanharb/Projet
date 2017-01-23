class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.key = (idteam,idplayer)
        self.middle= Vector2D()
    def my_position(self):
        return self.state.player_state(self.key[0],self.key[1]).position
        #equivalent a self.player_state(self.key[0],self.key[1])
    def ball_position(self):
        return self.state.ball.position
    def aller(self,p):
        return SoccerAction(p-self.my_position(),Vector2D())
    def shoot(self,p):
        return SoccerAction(Vector2D(),p-self.my_position())

    def position_but_adv(self):
        if self.key[0]==1:
            return(GAME_WIDTH,GAME_HEIGHT//2)
        else:
            return(0,GAME_HEIGHT//2)
    
    def positon_mon_but(self):
        if self.key[0]==1:
            return(0,GAME_HEIGHT//2)
        else:
            return(GAME_WIDTH,GAME_HEIGHT//2)

    def shoot_but_adv(self):
        self.shoot(self.position_but_adv(self.key[0]))
    
    def dist_player(self,p):
        return p.distance(self.my_position())
    
    def joueur_plus_proche(self):
        dmin=175
        for L in self.state.players :
            if L[0]==self.key[0] and L[1]!=self.key[1] and dmin>self.dist_player(state.player_state(L[0],L[1]).position) :
                dmin=self.dist_player(self.state.player_state(L[0],L[1]).position)
                player_proche=L
        return player_proche
    
    
                
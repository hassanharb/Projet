from soccersimulator import SoccerTeam
from golf import GolfStrat, SlalomStrat

def get_golf_team():
        team1 = SoccerTeam(name="France",login="etu1")
        team1.add("toti",GolfStrat())
        return team1
        
def get_slalom_team1():
        team1 = SoccerTeam(name="Liban",login="etu2")
        team1.add("totii",SlalomStrat())
        return team1

def get_slalom_team2():        
        team2 = SoccerTeam(name="Espagne",login="etu3")
        team2.add("Hassan",SlalomStrat())
        team2.add("Harb",SlalomStrat())
        return team2
from soccersimulator import SoccerTeam, SoccerAction
from strat import ElStrategy, ElDefenseur, ElStrategySolo,ElAilierDroit,ElAilierGauche,ElAttaquant4,ElDefenseur4


## Creation d'une equipe
team1 = SoccerTeam(name="Liban",login="Harb")
team2 = SoccerTeam(name="France",login="PE")
team4 = SoccerTeam(name="Gabon",login="Harouba")

team1.add("Hassan",ElStrategySolo())

team2.add("Paul",ElStrategy())
team2.add("Pogba",ElDefenseur())

team4.add("Hassan",ElDefenseur4())
team4.add("Booba",ElAilierDroit())
team4.add("Paul",ElAilierGauche())
team4.add("Pogba",ElAttaquant4())


def get_team(i):
    if i==1:
        return team1
    if i==2:
        return team2
    if i==4:
        return team4


from soccersimulator import SoccerTeam, Simulation, SoccerAction
from soccersimulator import SimuGUI,show_state,show_simu
from strat import fonceur, ElStrategy, ElDefenseur, Bestdeftest, ElLooser


## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Hassan",Bestdeftest())
team1.add("Booba",ElStrategy())
team2.add("Paul",ElLooser())
team2.add("Pogba",Bestdeftest())




#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
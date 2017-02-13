from soccersimulator import SoccerTeam, Simulation
from soccersimulator import SimuGUI,show_state,show_simu
from harbstrat import ElStrategy, ElDefenseur, ElLooser, ElStrategySolo


## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Hassan",ElLooser())
team1.add("Booba",ElLooser())
team2.add("Paul",ElStrategySolo())
team2.add("Pogba",ElDefenseur())



#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
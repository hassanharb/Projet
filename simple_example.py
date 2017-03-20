from soccersimulator import SoccerTeam, Simulation
from soccersimulator import SimuGUI,show_state,show_simu
from strat import ElStrategy, ElDefenseur, ElStrategySolo, ElLooser, ElAilierDroit,ElAilierGauche,ElAttaquant4,ElDefenseur4



## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team4 = SoccerTeam(name="team4",login="etu4")
team1.add("Hassan",ElStrategySolo())
team1.add("Booba",ElDefenseur())
team2.add("Paul",ElDefenseur())
team2.add("Pogba",ElLooser())

team4.add("Hassan",ElDefenseur4())
team4.add("Booba",ElAilierDroit())
team4.add("Paul",ElAilierGauche())
team4.add("Pogba",ElAttaquant4())



#Creation d'une partie
simu = Simulation(team4,team1)
#Jouer et afficher la partie
show_simu(simu)
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import SimuGUI,show_state,show_simu
#from harbstrat import ElStrategy, ElDefenseur, ElStrategySolo, ElLooser,ElAttaquant4,ElDefenseur4,ElAilierGauche2,ElAilierDroit2,ElAilierDroit,ElAilierGauche
from strat import ElStrategy, ElDefenseur, ElStrategySolo, ElLooser,ElAttaquant4,ElDefenseur4,ElAilierDroit,ElAilierGauche


## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team4 = SoccerTeam(name="team4",login="etu4")

team5 = SoccerTeam(name="team5",login="etu5")

team1.add("Hassan",ElStrategy())
team1.add("Booba",ElDefenseur())
team2.add("Paul",ElStrategySolo())
team2.add("Pogba",ElDefenseur())

team4.add("Hassan",ElDefenseur4())
team4.add("Booba",ElAilierDroit())
team4.add("Paul",ElAilierGauche())
team4.add("Pogba",ElAttaquant4())

#team5.add("Hassan2",ElDefenseur4())
#team5.add("Booba2",ElAilierDroit2())
#team5.add("Paul2",ElAilierGauche2())
#team5.add("Pogba2",ElAttaquant4())



#Creation d'une partie
simu = Simulation(team2,team1)
#Jouer et afficher la partie
show_simu(simu)
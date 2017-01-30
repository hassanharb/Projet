from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation, SoccerAction
from soccersimulator import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D
from soccersimulator.settings import *
from toolbox import MyState, Action
from strat import fonceur

## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Hassan",ElStrategy())
team2.add("Paul",ElStrategy())
team2.add("Pogba",ElLooser())

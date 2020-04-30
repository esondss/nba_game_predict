
from Game import Game
from Player import Player
from Team import Team
from NBA_Playoffs import WholeTournament
import time

# Group A
team1, team2 = Team('MIL'), Team('DET')

# Group B
team3, team4 = Team('BOS'), Team('IND')

# Group C
team5, team6 =T eam('PHI'), Team('BKN')

# Group D
team7, team8 = Team('TOR'), Team('ORL')

# Group E
team9, team10 = Team('GSW'), Team('LAC')

# Group F
team11, team12 =Team('HOU'), Team('UTA')

# Group G
team13, team14 = Team('POR'), Team('OKC')

# Group H
team15, team16 =Team('DEN'), Team('SAS')

# Create a tournament

tournament=WholeTournament()

# Create a simulation loop

def run(n_simulations):
    i=0
    while i<=n_simulations:
        tournament.tournament.one_time_simu(

        (team1, team2), (team3, team4),
        (team5, team6), (team7, team8),
        (team9, team10),(team11, team12),
        (team13, team14),(team15, team16)

        )

    return 'Finished.\n \
            Total run time: {:.2f}s'.format(time.time()-start_time)

# Run 1,000 simulation
run(1000)

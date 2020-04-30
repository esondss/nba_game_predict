
#  NBA Game Predict (MLH Hackathon)

## Introduction

This repo uses a Simu/ML model to predict an NBA game or even the entire NBA playoffs tournament. We will need to specify the estimated distributions of each team's abilities based on 10 features, all of which should range from 0 to 1 except for the last one "PF" being an integer. All features are defaulted to 0. One can check what features are included in 'info.txt'.

## Design

This Repo has Six basic components:

- **Player**: To define a player with a set of attributes.
- **Team**: To define a team whose attributes can be initialized either through itself or a list of players.
- **Randomizers**: To create simulated variates based on various distributions.
- **Models**: To predict Win/Loss based on team features.
- **Game**: To run a stand-alone game between two teams and output Win/Loss for the first team.
- **NBA Playoffs**: To run multiple games based on the rules of NBA final tournament.

## How To Use

In order to predict any game with this repo, a three-step process would apply: <br>

(1) Create two or more team objects. <br>
(2) Define their attributes. <br>
(3) Run game. <br>

### Step 1: Create Team

To create a team called Golden State Warrior, we simply call `GSW = Team('Golden State Warrior')`. <br>
A name is a required argument for simulation purposes.

### Step 2: Define Abilities

We can define a team's abilities at "team's level" or "players' level". <br>
Simply access the attribute of a team by calling the class attribute e.g. `GSW.TwoPointPercentage `. <br>
To simulate a number, a linear equation is applied: `bias + coefficient * variate`:

- `bias` is a rudimentary argument passed in by the user.
- To return the same number every time, just pass in `bias={a number}` , `coefficient` is defaulted to 0.
- To return a different number every time, we need two more arguments  `distribution_type` and `paras` and set `coefficient` > 0.
- Check what types of distributions are included in 'info.txt'.
- The simulated variate will automatically update the object atrribute.

**Predict From Team:** <br>
- Let's say we want to simulate a value of Two Point Percentage which follows " 2PP = 0 + 1 * Normal Distribution (0.2, 0.6) ".<br>
- First we will call `GSW.init_2PP(bias=0, coefficient=1, distribution_type='normal', paras=(0.2, 0.6))`. <br>
- Then we can simulate the value with `GSW.simu_2PP()`.

**Predict From Players**:

We can also initialize variates at players' level instead of team's level.

1. Let's create two players `Joe=Player('Joe')` and `Ben=Player('Ben')`.
2. Specify their attribute by running `Joe.init_2PP(...)`, the same way as we would do to a team.
3. To simulate variate from a list of players:
    - We first call `GSW.team_up([Joe, Ben])` which assigns the players to a team Golden State Warrior (GSW).
    - Then we can simulate the value with `GSW.simu_2PP_from_players()`.


### Step 3: Predict Game

Say whe have two teams (GSW, HOU) with defined attributes:

1. To create a game: `game=Game(GSW, HOU)`.
2. To predict result: `game.predict(num_games)` with `num_games` being the number of games we want them to play.

## Simulating NBA Final Tournament

This repo includes off-the-shelf module to simulate the entire NBA final tournament. A few things to be noted:

- There should be 16 teams, each with defined attributes.
- We need to initialize 8 team-pairs for the initial round. (team1, team2), (team3, team4) ... etc.
- Every group by default will play 7 times for NBA playoffs is a best of 7 elimination process.

**Create A Tournament:**

1. Create a tournament: `tournament=WholeTournament()`

2. See who will be the Playoffs Champion by passing 8 groups (16 teams) with defined attributes:
    - `Champion=tournament.one_time_simu( (team1, team2),...(team15, team16) )`
    - `print(Champion)`

**Simulate Tournament N times**

- We can use a loop to simulate the tournament N times by running `tournament.one_time-simu` N times. <br>
- The results of every simulation will be stored in the object tournament's attributes as lists.
- Probabilities can be calculated by assessing the number of times a team shows up in each round's winning list.
- See 'SimuExample.py' for an example.

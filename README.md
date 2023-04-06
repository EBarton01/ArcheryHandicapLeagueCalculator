# ArcheryHandycapLeagueCalculator
Program to calculate league scores using a handicap system.
Uses pysimple gui as a basic gui system. Allows for imports of formatted .json files. These files contain a dictionary with league information.
keep the .json files in same folder as program for ease of import. To import type in just filename, no need to add .json to the name.

Information is saved as: 
Team#:
   Shooter#:
      Name: NULL
      Week#: {'Handycap:': (calculates HC based on week), 'Score:': [(score before handycap), (score after handycap)]}
      
Team size ranges 1 - 3. Max points set to 300. Amount of teams 1 - 50.
Delete week currently deletes the most current week.

V1.0.0: issue known with editing points. if changes made to non current week, all subsequent weeks must be updated for the whole team.


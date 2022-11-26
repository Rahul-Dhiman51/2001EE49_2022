import openpyxl
import pandas as pd
import os
from datetime import datetime
start_time = datetime.now()
india_innings = open("india_inns2.txt","r+")    #opening india innings file
pakistan_innings = open("pak_inns1.txt","r+")   #opening pakistan innings file
teamss = open("teams.txt","r+")
input_teams = teamss.readlines()

pakistan_team = input_teams[0]
pakistan_players = pakistan_team[23:-1:].split(",")

india_team = input_teams[2]
india_players = india_team[20:-1:].split(",")


first_india=india_innings.readlines()   #reading india innings file
for i in first_india:
    if i=='\n':
        first_india.remove(i)







#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))

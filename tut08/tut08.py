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

first_pakistan=pakistan_innings.readlines()     #reading pakistan innings file
for i in first_pakistan:
    if i=='\n':
        first_pakistan.remove(i)

wb = openpyxl.Workbook()
spreadsheet = wb.active

    #   batting [runs,ball,4s,6s,sr]
    #   bowling [over,medan,runs,Wickets, NB, WD, ECO]
india_fall_of_wickets=0
pakistan_fall_of_wickets=0
out_pakistan_bat={}
india_bowlers={}
india_bats={}

pakistan_bats={}
pakistan_bowlers={}
pakistan_byes=0
pakistan_bowlers_total=0
for k in first_pakistan:
    t=k.index(".")
    overs_pakistan=k[0:t+2]
    temp=k[t+2::].split(",")
    current_ball=temp[0].split("to")





#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))

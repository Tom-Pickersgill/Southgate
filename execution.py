"""
The execution file from which all data analysis is run
"""
import pdb, importlib
import pandas as pd
import numpy as np
from tools.ReadDataFromURL import DataTools
from tools.PlayerPortGen import PlayerPort
from tools.DataAnalysis import DataAnalysisToolkit
from database.database_tools import DatabaseTools

DB = DatabaseTools(r'database/southgate_db.db','FPL_data')

""" Backtest Parameters """

params = {'bt_start_week':'Y17W0',
          'bt_start_year':'Y17W37'}


first_XI =    [['Joe','Hart','WHU'],
              ['Daley','Blind','MUN'],
              ['Ryan','Betrand','SOU'],
              ['Geoff','Cameron','STK'],
              ['Jonathan','Leko','WBA'],
              ['Kevin','Mirallas','EVE'],
              ['Henrikh','Mkhitaryan','MUN'],
              ['Ahmed','Musa','LEI'],
              ['Charly','Musonda','CHE'],
              ['Harry','Kane','TOT'],
              ['Danny','Ings','LIV'],
]

subs = [['Stuart','Taylor','SOU'],
        ['Craig','Cathcart','WAT'],
        ['Leroy','Fer','SWA'],
        ['Marko','Grujic','LIV']]

player_port_df = PlayerPort(first_XI, subs, 'Y17W0', DB)

#query_dict = {'FirstName':['Almen','Charlie'],'Surname':['Salah','Afellay']}


df = pd.read_csv('gamelogs/complete_data.csv')

DA = DataAnalysisToolkit(df)

DT = DataTools()



#DT.GenerateFullCSV()\
#df = DT.HistoricalData({'2016': '5-10', '2017': '0-5'})
#DT.RemoveColumns({'2016':'5-37', '2017':'0-37', '2018':'0-0'}, 'GW')
#
#
#df_full['TopPointsPerPrice']= df_full.PointsLastRound / df_full.Cost * 1e6
#
#grp = df_full.groupby(['Surname'])['TopPointsPerPrice'].mean()
#
#df_small = df_full[df_full['Surname'].isin(grp.nlargest(5).index)]
#
#df_new = pd.DataFrame()
#for name in grp.nlargest(5).index:
#    df_new[name] = df_full.loc[df_full['Surname'] == name]['TopPointsPerPrice']
#    
#for gameweek in df_test.index.unique():
#    print(df_test.loc[gameweek]['Surname'].unique())
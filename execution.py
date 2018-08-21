"""
The execution file from which all data analysis is run
"""
import pdb, importlib
import pandas as pd
from tools.ReadDataFromURL import DataTools
from tools.MemoryOptimiser import type_reduct_dict
from tools.DataAnalysis import DataAnalysisToolkit
from database.database_tools import DatabaseTools


def filter_df(df, query_dict):
    for key, values in query_dict.items():
        if not 'mask' in locals(): mask = df[key].isin(values)
        else: mask = mask | df[key].isin(values)

    return df[mask]

""" Backtest Parameters """
params = {'bt_start_week':'',
          'bt_start_year':'',
          'squad':'',
          'subs':''}


query_dict = {'FirstName':['Almen','Charlie'],'Surname':['Salah','Afellay']}


df = pd.read_csv('gamelogs/complete_data.csv')
DA = DataAnalysisToolkit(df)
DB = DatabaseTools(r'database/southgate_db.db','FPL_data')
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
"""
The execution file from which all data analysis is run
"""
#import pdb
from tools.ReadDataFromURL import DataTools as DT
from tools.MemoryOptimiser import type_reduct_dict

#df = DT.LatestData()
#df_full = DT.LoadFullData()
#DT.GenerateFullCSV()
var = DT.HistoricalData({'2016': '5-10', 
                         '2017': '0-5'})
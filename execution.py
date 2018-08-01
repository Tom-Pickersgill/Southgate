"""
The execution file from which all data analysis is run
"""

from tools.ReadDataFromURL import DataTools as DT

Var = DT.LatestData()
DT.GenerateFullCSV()

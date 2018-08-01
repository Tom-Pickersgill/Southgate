""" Tools for importing the latest or historical FPL data """
import urllib.request, json, os, pdb
import pandas as pd

class DataTools():
    
    def LatestData():
        """ Returns Dataframe object of latest FPL data """
        
        link = u"https://fantasy.premierleague.com/drf/elements"
        
        with urllib.request.urlopen(link) as url:
            return  pd.DataFrame(json.loads(url.read().decode()))
        
    def HistoricalData(game_week=[], year=[]):
        """
        Returns Dataframe object for historical FPL data. 
        Vargin for game_week and year must be python list.
        Pass no arguements to return full historical df.
        """
        if game_week == year == []:
            return pd.read_csv()
       
    def GenerateFullCSV():
        """ Generates an updated CSV from all saved CSVs """

        log_dir = os.listdir('./gamelogs')      
        ignore = ['__init__.py', 'complete_data.csv']
        csv_list = [x for x in log_dir if x not in ignore]
        
        df = pd.DataFrame()

        for file in csv_list:
            df = df.append(pd.read_csv('./gamelogs/'+file), sort=False)

        df.to_csv('./gamelogs/complete_data.csv')

    def LoadFullData():
        """ Returns dataframe containing all historical data """
        return pd.read_csv('./gamelogs/complete_data.csv')

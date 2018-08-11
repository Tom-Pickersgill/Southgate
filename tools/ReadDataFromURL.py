""" Tools for importing the latest or historical FPL data """
import urllib.request, json, os, pdb
import pandas as pd

class DataTools():
    
    def LatestData():
        """ Returns Dataframe object of latest FPL data """
        
        link = u"https://fantasy.premierleague.com/drf/elements"
        
        with urllib.request.urlopen(link) as url:
            return pd.DataFrame(json.loads(url.read().decode()))
        
    def HistoricalData(year_week_dict):
        """
        Returns Dataframe object for historical FPL data. 
        Input arg must be dict where key='yyyy', value='X-N'
        """

        for year, weeks in year_week_dict.items():
            for i, week in enumerate(weeks.split('-')):
                log_name = ('FPL{}-GW{}.csv').format(year[2:],week)

                if not 'df' in locals():
                    df = pd.read_csv('./gamelogs/'+log_name)
                else:
                    df = pd.concat([df, pd.read_csv('./gamelogs/'+log_name)],
                                    join='inner')
            
        return df
       
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

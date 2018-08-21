""" Tools for importing the latest or historical FPL data """
import urllib.request, json, os, pdb
import pandas as pd

class DataTools():

    def __init__(self):
        self.name = 'Tom'

    def LatestData(self):
        """ Returns Dataframe object of latest FPL data """

        link = u"https://fantasy.premierleague.com/drf/elements"

        with urllib.request.urlopen(link) as url:
            return pd.DataFrame(json.loads(url.read().decode()))


    def HistoricalData(self, year_week_dict):
        """
        Returns Dataframe object for historical FPL data.
        Input arg must be dict where key='yyyy', value='X-N'
        """

        from tools.MemoryOptimiser import df_dtypes

        for year, weeks in year_week_dict.items():
            for week in range(int(weeks.split('-')[0]),
                              int(weeks.split('-')[1])+1):
                log_name = ('FPL{}-GW{}.csv').format(year[2:], week)

                if not 'df' in locals():
                    df = pd.read_csv('./gamelogs/'+log_name,
                                     dtype=df_dtypes)
                    if not 'ICTIndex' in df.columns:
                        df['ICTIndex'] = 0

                else:
                    df_new = pd.read_csv('./gamelogs/'+log_name,
                                                dtype=df_dtypes)
                    
                    if not 'ICTIndex' in df_new.columns:
                        df_new['ICTIndex'] = 0
                    
                    df = pd.concat([df, df_new],
                                   join='inner', sort=False)
                    
        
        #df.set_index(['year','week'], inplace=True)
        
        return df.astype(df_dtypes)

    def GenerateFullCSV(self):
        """ Generates an updated CSV from all saved CSVs """

        df = self.HistoricalData({#'2016':'5-37',
                                #'2017':'0-37',
                                '2018':'1-1'})

        df.to_csv('./gamelogs/complete_data.csv', index=False)

        return df

    def LoadFullData(self):
        """ Returns dataframe containing all historical data """

        return pd.read_csv('./gamelogs/complete_data.csv')


    def RemoveColumns(self, year_week_dict, text):
        """ Removes columns in raw data """
        for year, weeks in year_week_dict.items():
               for week in range(int(weeks.split('-')[0]),
                                 int(weeks.split('-')[1])+1):
                    log_name = ('FPL{}-GW{}.csv').format(year[2:],week)
                    df = pd.read_csv('./gamelogs/'+log_name)
                    cols = [c for c in df.columns if c[:2] != text]
                    df = df[cols]
                    df.to_csv('./gamelogs/'+log_name, index=False)


    def AddWeekYear(self, year_week_dict):
        """ Removes columns in raw data """
        for year, weeks in year_week_dict.items():
               for week in range(int(weeks.split('-')[0]),
                                 int(weeks.split('-')[1])+1):
                    log_name = ('FPL{}-GW{}.csv').format(year[2:],week)
                    df = pd.read_csv('./gamelogs/'+log_name)
                    df['year'] = year
                    df['week'] = week
                    df['Timeline'] = ('Y'+df.year.astype(str).str[2:] +
                                      'W'+df.week.astype(str))
                    df.to_csv('./gamelogs/'+log_name, index=False)

    def uploadAllData(self, year_week_dict, DB):
        """ Removes columns in raw data """
        for year, weeks in year_week_dict.items():
               for week in range(int(weeks.split('-')[0]),
                                 int(weeks.split('-')[1])+1):
                    log_name = ('FPL{}-GW{}.csv').format(year[2:],week)
                    pdb.set_trace()
                    df = pd.read_csv('./gamelogs/'+log_name)
                    DB.upload(df)
                    df['Timeline'] = ('Y'+df.year.astype(str).str[2:] +
                                      'W'+df.week.astype(str))
                    df.to_csv('./gamelogs/'+log_name, index=False)
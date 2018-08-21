import seaborn as sns
sns.set()

class DataAnalysisToolkit():
    
    def __init__(self, df):
        self.df = df
        self.filtered_df = None
        
        
    def filter_df(self, df, query_dict):
        """ Filters dataframe to include only supplied conditionals
            query_dict is dict object type, with the keys column variables
            and values either a string, value or list type. """
            
        for key, values in query_dict.items():
            if not 'mask' in locals(): mask = self.df[key].isin(values)
            else: mask = mask | self.df[key].isin(values)
    
        self.filtered_df = self.df[mask]
        return df[mask]
    
        
    def TopPointsPerPrice(self, df, number_players=10):
        df['TopPointsPerPrice']= df.PointsLastRound / df.Cost / 1e6
        
    def MatchCoverage(self, player_list):
        """ Returns graph of player coverage from the start of 
            2016/17 season. """
            
        #x[x.index.get_level_values(0) == 'Aaron']
        grp = self.df.groupby(['FirstName','Surname']).size()
        
        num_matches = self.df.index.value_counts().size
        return 100/num_matches
        
        
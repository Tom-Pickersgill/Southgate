import seaborn as sns

class DataAnalysisToolkit():
    
    def __init__(self, df):
        self.df = df
        sns.set()
        
    def TopPointsPerPrice(self, df, number_players=10):
        df['TopPointsPerPrice']= df.PointsLastRound / df.Cost / 1e6
        
    def MatchCoverage(self, player_list):
        """ Returns graph of player coverage from the start of 
            2016/17 season. """
            
        #x[x.index.get_level_values(0) == 'Aaron']
        grp = self.df.groupby(['FirstName','Surname']).size()
        
        num_matches = self.df.index.value_counts().size
        return 100/num_matches
        
        
import pandas as pd
import time, pdb

def PlayerPort(squad, params, df_uni, DB, use_pandas=True):
    """ PlayerPort function constructs a df containing FF squad info 
        through time. Pass output to backtest engine for performance
        through time.
    """
    first_XI = squad[0]
    subs = squad[1]
    "~~~~~~~~~~~~~~~~~~~~ Filter Universe ~~~~~~~~~~~~~~~~~~~~"
    """ This section is used when querying is done via pandas and not SQL """
    
    if use_pandas:
        df = df_uni[df_uni['Timeline'].isin([params['bt_start']])]
        #df = df_uni[df_uni['Timeline'].isin(TimelineList(params))]
        df = df[df['FirstName'].isin([x[0] for x in first_XI])]
        df = df[df['Surname'].isin([x[1] for x in first_XI])]


    "~~~~~~~~~~~~~~~~~~~~ Construct the Dataframe ~~~~~~~~~~~~~~~~~~~~"

    df_out = pd.DataFrame(columns=[start_date],
                          index=['First_XI','Subs','Budget','Free_T'])
    
    df_out.at['First_XI', start_date] = first_XI
    df_out.at['Subs', start_date] = subs
    df_out.at['Free_T', start_date] = 0
    df_out.at['Budget', start_date] = BudgetCalc(df, df_out, DB)
    
    "~~~~~~~~~~~~~~~~~~~~ Specify and check Constraints ~~~~~~~~~~~~~~~~~~~~"
    
    return df_out if checkConstraints else False

def BudgetCalc(df_universe, df_squad, DB):
    """ Returns initial squad cost """
    
    df_query = DB.query()

def checkConstraints(df):
    max_pos = {'GK':2, 'Def':5, 'Mid':5, 'Atk':3}
    max_players_per_team = 3
    max_players = 11
    num_subs = 4
    max_players_per_pos = {'GK':1, 'Def':5, 'Mid':5, 'Atk':3}
    min_players_per_pos = {'GK':1, 'Def':3, 'Mid':3, 'Atk':1}
    
    
    
def Backtest(params, print_analysis=False):
    """ Creates the squad through time """
    
    return df_out



def Optimiser(df):
    """ Returns optimised player port based on constraints """
    
    #Insert Machine Learning Algo here 
    
    
    return df_out

def TimelineList(params):

    start_year = int(params['bt_start'][1:3])
    end_year   = int(params['bt_end'][1:3])
    time_list = []
    
    for year in range(start_year, end_year+1):
        start_week = int(params['bt_start'].split('W')[1]) if year != start_year else 0
        end_week   = int(params['bt_end'].split('W')[1]) if year != end_year else 37
        for week in range(start_week,end_week+1):
            time_list.append('Y{}W{}'.format(year, week))
    
    return time_list


import pandas as pd

def PlayerPort(first_XI, subs, params, DB):
    """ PlayerPort function constructs a df containing FF squad info 
        through time. Pass output to backtest engine for performance
        through time.
    """
    
    "~~~~~~~~~~~~~~~~~~~~ Construct the Dataframe ~~~~~~~~~~~~~~~~~~~~"

    df_out = pd.DataFrame(columns=[start_date],
                          index=['First_XI','Subs','Budget','Free_T'])
    
    df_out.at['First_XI', start_date] = first_XI
    df_out.at['Subs', start_date] = subs
    df_out.at['Free_T', start_date] = 0
    df_out.at['Budget', start_date] = BudgetCalc(df_out)
    
    "~~~~~~~~~~~~~~~~~~~~ Specify and check Constraints ~~~~~~~~~~~~~~~~~~~~"
    
    return df_out if checkConstraints else False

def BudgetCalc(df, DB):
    """ Returns initial squad cost """
    
    #query_dict = {'FirstName':df.FirstName,
                   'Surname':df.Surname}
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
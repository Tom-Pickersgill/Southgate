import pandas as pd
import pprint


def mem_usage(pandas_obj):

    if isinstance(pandas_obj, pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else: # we assume if not a df it's a series
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b / 1024 ** 2 # convert bytes to megabytes
    return int(usage_mb)

def cached_date_parser(s):
    """ Function passed to date_parser vargin for pd.read_csv to quickly 
        convert all dates to datetime format instead of string. """
        
    if not'date_cache' in globals():
        globals()['date_cache'] = {}
        
    if s in date_cache:
        return date_cache[s]
    dt = pd.to_datetime(s, format='%d/%m/%Y', errors='coerce')
    date_cache[s] = dt
    return dt

def type_reduct_dict(gl, date_col_name='', csv_date_format='%d/%m/%Y'):

    gl_int = gl.select_dtypes(include=['int'])
    converted_int = gl_int.apply(pd.to_numeric,downcast='unsigned')

    gl_float = gl.select_dtypes(include=['float'])
    converted_float = gl_float.apply(pd.to_numeric,downcast='float')

    optimized_gl = gl.copy()

    optimized_gl[converted_int.columns] = converted_int
    optimized_gl[converted_float.columns] = converted_float

    print(('Memory saving on floats and ints = {} MB'
           ).format(mem_usage(gl)-mem_usage(optimized_gl)))

    gl_obj = gl.select_dtypes(include=['object']).copy()

    converted_obj = pd.DataFrame()

    for col in gl_obj.columns:
        num_unique_values = len(gl_obj[col].unique())
        num_total_values = len(gl_obj[col])
        if num_unique_values / num_total_values < 0.5:
            converted_obj.loc[:,col] = gl_obj[col].astype('category')
        else:
            converted_obj.loc[:,col] = gl_obj[col]


    print(('Memory saving on objects = {} MB'
          ).format(mem_usage(gl_obj)-mem_usage(converted_obj)))

    compare_obj = pd.concat([gl_obj.dtypes,converted_obj.dtypes],axis=1)
    compare_obj.columns = ['before','after']
    compare_obj.apply(pd.Series.value_counts)

    optimized_gl[converted_obj.columns] = converted_obj

    print(("{:03.2f} % reduction in df memory compared to original"
           ).format((1-mem_usage(optimized_gl)/mem_usage(gl))*100))

    if date_col_name:
        date = optimized_gl.dates
        optimized_gl['dates'] = pd.to_datetime(date,format=csv_date_format)
        dtypes = optimized_gl.drop('dates',axis=1).dtypes
    else:
        dtypes = optimized_gl.dtypes

    dtypes_col = dtypes.index
    dtypes_type = [i.name for i in dtypes.values]

    column_types = dict(zip(dtypes_col, dtypes_type))
    preview = {key:value for key,value in list(column_types.items())}

    pp = pprint.PrettyPrinter(indent=4)
    print("""Remember to pass pd.read_csv(path, parse_dates=['dates'],
          infer_datetime_format=True OR date_parser=cached_date_parser) 
          as well as dtype=col_type_dict""")
    print(" ")
    pp.pprint(preview)
    
    return preview

df_dtypes = {
    'Assists': 'int64',
    'AveragePoints': 'float32',
    'AveragePointsPerDollar': 'float32',
    'BPS': 'int64',
    'Bonus': 'int64',
    'CleanSheetPoints': 'int64',
    'CleanSheets': 'int64',
    'Cost': 'int64',
    'DreamteamCount': 'int64',
    'EAIndex': 'int64',
    'FanRating': 'int64',
    'FirstName': 'category',
    'Form': 'float32',
    'GameweekWeighting': 'int64',
    'GoalsConceded': 'int64',
    'GoalsConcededPoints': 'int64',
    'GoalsScored': 'int64',
    'GoalsScoredPoints': 'int64',
    'LastSeasonPoints': 'int64',
    'MinutesPlayed': 'int64',
    'NextFixture1': 'category',
    'NextFixture2': 'category',
    'NextFixture3': 'category',
    'NextFixture4': 'category',
    'NextFixture5': 'category',
    'OwnGoals': 'int64',
    'PenaltiesMissed': 'int64',
    'PenaltiesSaved': 'int64',
    'PointsLastRound': 'int64',
    'PositionsList': 'category',
    'PriceFall': 'int64',
    'PriceFallRound': 'int64',
    'PriceRise': 'int64',
    'PriceRiseRound': 'int64',
    'RedCards': 'int64',
    'Saves': 'int64',
    'SavesPoints': 'int64',
    'SelectedByPercent': 'float32',
    'Surname': 'category',
    'Team': 'category',
    'Timeline': 'category',
    'TotalPoints': 'int64',
    'TotalPointsPerDollar': 'float32',
    'TransfersIn': 'int64',
    'TransfersInRound': 'int64',
    'TransfersOut': 'int64',
    'TransfersOutRound': 'int64',
    'ValueForm': 'float32',
    'ValueSeason': 'float32',
    'YellowCards': 'int64'}
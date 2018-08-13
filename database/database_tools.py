import sqlite3, time, pdb
from database.tableclasses import FPL_data_table
from sqlalchemy import create_engine

class DatabaseTools():
    """ A set of databse connection tools """
    
    def __init__(self, db_name, table_name):
        
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        #self.engine = create_engine('sqlite://', echo=False)
        
        if table_name is 'FPL_data':
            self.table_class = FPL_data_table()
        else: self.table_class = None

        
    def create_table(self, table_class=None):
        if self.table_name is 'FPL_data': table_class = FPL_data_table()
        self.c.execute('CREATE TABLE IF NOT EXISTS {}({})'
                  .format(self.table_name, table_class))

    def data_entry(self, values):
        self.c.execute('INSERT INTO {} VALUES({})'.format(self.table_name, values))
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def drop_table(self):
        self.c.execute('DROP TABLE IF EXISTS {}'.format(self.table_name))

    def upload(self, df):
        start = time.time()
        df.to_sql(self.table_name, self.conn, if_exists='replace')
        print('Time for upload: {}s'.format(time.time()-start))
        pdb.set_trace()
        self.conn.commit()
        self.c.close()
        self.conn.close()

def create_connection(db_file):
    from sqlite3 import Error
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None 

create_connection(r'C:\Users\Tom\Python\southgate\database\Southgate_db.db')
#create_table('FPL_data', FPL_data_table())
#drop_table('FPL_data')

import sqlite3, time, pdb
from database.tableclasses import FPL_data_table
#from sqlalchemy import create_engine

class DatabaseTools():
    """ A set of databse connection tools """
    
    def __init__(self, db_name, table_name):
        
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        #self.engine = create_engine('sqlite://', echo=False)
        
        if table_name is 'FPL_data':
            self.table_class = FPL_data_table()
        else: self.table_class = None

        
    def create_table(self, table_class=None):
        if self.table_name is 'FPL_data': table_class = FPL_data_table()
        self.cur.execute('CREATE TABLE IF NOT EXISTS {}({})'
                  .format(self.table_name, table_class))
        self.conn.commit()
        
    def data_entry(self, values):
        self.cur.execute('INSERT INTO {} VALUES({})'
                       .format(self.table_name, values))
        self.conn.commit()

    def drop_table(self):
        self.cur.execute('DROP TABLE IF EXISTS {}'.format(self.table_name))

    def upload(self, df):
        start = time.time()
        df.to_sql(self.table_name, self.conn, if_exists='replace')
        print('Time for upload: {}s'.format(time.time()-start))
        self.conn.commit()
        
    def fetchall(self):
        return self.cur.fetchall()
        
    def close(self):
        self.cur.close()
        self.conn.close()

    def query(self, query_dict):
        for key, value in query_dict.items():
            self.cur.execute("Select * from {} where {} = '{}'".
                             format(self.table_name, key, value))
        return self.cur.fetchall()

    def return_col_names(self):
        self.cur.execute('PRAGMA TABLE_INFO({})'.format(self.table_name))
        return self.fetchall()

    def count_total_rows(self, print_out=False):
        """ Returns the total number of rows in the database """
        self.cur.execute('SELECT COUNT(*) FROM {}'.format(self.table_name))
        count = self.fetchall()
        
        if print_out:
            print('\nTotal rows: {}'.format(count[0][0]))
            
        return count[0][0]
    
#create_table('FPL_data', FPL_data_table())
#drop_table('FPL_data')

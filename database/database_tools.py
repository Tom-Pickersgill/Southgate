import sqlite3
from tableclasses import FPL_data_table
from sqlalchemy import create_engine




class DatabaseTools():
    """ A set of databse connection tools """
    
    def __init__(self, db_name, table_name):
        
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.engine = create_engine('sqlite://', echo=False)
        
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


#create_table('FPL_data', FPL_data_table())
#drop_table('FPL_data')

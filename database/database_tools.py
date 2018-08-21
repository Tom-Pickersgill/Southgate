from database.tableclasses import FPL_data_table
import sqlite3, time, pdb
import pandas as pd

class DatabaseTools():
    """ A set of databse connection tools """
    
    def __init__(self, db_name, table_name):
        
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        
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
        df.to_sql(self.table_name, self.conn, if_exists='append', index=False)
        print('Time for upload: {}s'.format(time.time()-start))
        self.conn.commit()
        
    def fetchall(self):
        return self.cur.fetchall()
        
    def close(self):
        self.cur.close()
        self.conn.close()

    def query(self, query_dict={}, join_type='OR', return_df=True, sort_on="",
              sort_type="", limit=""):
        """ sort type = asc or desc
            supply empty query dict to return all data in db
        """

        where = 'where' if query_dict else ''
        query = "Select * from {} {} ".format(self.table_name, where) +\
                " {} ".format(join_type).join(
                ["{}='{}'".format(key, value)
                for key in query_dict
                for value in query_dict[key]])
    
        if sort_on: query += "order by {}".format(sort_on)
        if sort_on and sort_type: query += " " + sort_type
        if limit: query += "limit " + limit
        
        if return_df:
            return pd.read_sql_query(query, self.conn)
        else:
            self.cur.execute(query)
            return self.cur.fetchall()

    def return_col_names(self):
        self.cur.execute('PRAGMA TABLE_INFO({})'.format(self.table_name))
        return self.fetchall()

    def count_total_rows(self):
        """ Returns the total number of rows in the database """
        self.cur.execute('SELECT COUNT(*) FROM {}'.format(self.table_name))
        count = self.fetchall()
            
        return count[0][0]

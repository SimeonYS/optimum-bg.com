
import sqlite3

class OptimumPipeline(object):


    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("opti.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS optimum_advertising """)
        self.curr.execute("""create table optimum_advertising(
                        title text,
                        desription text
                         )
                        """)

    def process_item(self,items,spider):
        self.store_db(items)
        return items

    def store_db(self,items):
        self.curr.execute("""insert into optimum_advertising values (?,?)""" ,(
            items['title'][0],
            items['description']
        )
        )
        self.conn.commit()





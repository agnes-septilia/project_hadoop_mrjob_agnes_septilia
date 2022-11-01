"""
MRJOB TASK 2: Aggregate TR_OrderDetails.csv transaction quantity based on date
"""


### import libraries 
from mrjob.job import MRJob
import psycopg2


### define mrjob
class MRAggregateDate(MRJob):

    # define the connection
    def reducer_init(self):
        self.conn = psycopg2.connect(database="project4", user="postgres", password="1234", host="host.docker.internal", port="5430")

    # take only order date and quantity
    def mapper(self, _, line):
        item = line.strip().split(',')
        if item[4] == 'Quantity':
            pass
        else:    
            year = item[1][-4:]
            yield year, int(item[4])
    
    # aggregate the result
    def reducer(self, key, values):
        self.cur = self.conn.cursor()
        self.cur.execute("insert into total_order_yearly (order_date, total_order) values(%s, %s)", (key, sum(values)))
        # yield key, sum(values)
 
    # commit the connection
    def reducer_final(self):
        self.conn.commit()
        self.conn.close()


### run the mrjob
if __name__ == '__main__':
   MRAggregateDate.run()

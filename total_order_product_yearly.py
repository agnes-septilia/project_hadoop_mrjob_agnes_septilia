"""
MRJOB TASK 3: Aggregate TR_OrderDetails.csv transaction quantity based on date and product 
"""


### import libraries 
from mrjob.job import MRJob
import psycopg2


### define mrjob
class MRAggregateProductDate(MRJob):

    # define the connection
    def reducer_init(self):
        self.conn = psycopg2.connect(database="project4", user="postgres", password="1234", host="localhost", port="5430")

    # take only order date and quantity
    def mapper(self, _, line):
        item = line.strip().split(',')
        if item[4] == 'Quantity':
            pass
        else:    
            year = item[1][-4:]
            product = item[3]
            yield (year, product), int(item[4])
    
    # aggregate the result
    def reducer(self, key, values):
        self.cur = self.conn.cursor()
        self.cur.execute("insert into total_order_product_yearly (order_date, product_id, total_order) values(%s, %s, %s)", (key[0], key[1], sum(values)))
        # yield key, sum(values)
 
    # commit the connection
    def reducer_final(self):
        self.conn.commit()
        self.conn.close()


### run the mrjob
if __name__ == '__main__':
   MRAggregateProductDate.run()

### import libraries
from ast import Index
from xmlrpc.client import DateTime
import pandas as pd 
from sqlalchemy import create_engine


### load data
mrjob_task_1 = pd.read_csv('~/Documents/digital_skola/Project/project_4/mrjob_task_1.csv')
mrjob_task_2 = pd.read_csv('~/Documents/digital_skola/Project/project_4/mrjob_task_2.csv')
# mrjob_task_3 = pd.read_csv('~/Documents/digital_skola/Project/project_4/mrjob_task_3.csv')


### change column name to lowercase
mrjob_task_1.columns = ['product_id', 'product_name', 'product_category', 'price']
mrjob_task_2.columns = ['order_date', 'quantity']


### change column type as date for date-based value
mrjob_task_2['order_date'] = pd.to_datetime(mrjob_task_2['order_date'], format='%d-%m-%Y')

# print(mrjob_task_1)
# print(mrjob_task_2)


### create engine to upload table content
engine = create_engine(f'postgresql://{"postgres"}:{"1234"}@{"localhost"}:{"5430"}/{"project4"}')


### insert new data to postgres
mrjob_task_1.to_sql("mrjob_task_1", engine, if_exists="replace", index=False)
mrjob_task_2.to_sql("mrjob_task_2", engine, if_exists="replace", index=False)

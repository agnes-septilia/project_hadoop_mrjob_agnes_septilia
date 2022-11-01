### import libraries
import pandas as pd 
from sqlalchemy import create_engine


### load data 
tr_products = pd.read_csv('~/Documents/digital_skola/Project/project_4/dataset_project_4/TR_Products.csv')
tr_user_info = pd.read_csv('~/Documents/digital_skola/Project/project_4/dataset_project_4/TR_UserInfo.csv')

# change column name to lowercase
tr_products.columns = ['product_id', 'product_name', 'product_category', 'price']
tr_user_info.columns = ['user_id', 'user_sex', 'user_device']

# print(tr_products)
# print(tr_user_info)


## create engine to upload table content
engine = create_engine(url='postgresql://postgres:1234@localhost:5430/project4')

## insert new data to postgres
tr_products.to_sql("tr_products", engine, if_exists="replace", index=False)
tr_user_info.to_sql("tr_user_info", engine, if_exists="replace", index=False)

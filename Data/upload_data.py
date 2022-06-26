import pandas as pd
from sqlalchemy import create_engine
import pymysql

location = 'heart_2020_cleaned.csv'
data = pd.read_csv(location)

host = '127.0.0.1'
user = 'root'
password = 'vptmdnjem*!123'
database = 'sys'

pymysql.install_as_MySQLdb()

table_name = 'heart_disease_2020'
engine = create_engine(f'mysql+mysqldb://{user}:{password}'\
                f'@{host}:3306/{database}',
                encoding='utf-8')

data.to_sql(name=table_name,
        con=engine,
        if_exists='append',
        index=False)

engine.dispose()


"""
Python_Uploading_Csv_File_To_Snowflake - Python Project To Upload Files To Snowflake Using Python.
"""

import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
conn = snowflake.connector.connect(
    user = 'USERNAME_YOU_AUTHENTICATE_AS',
    password = 'PASSWORD_YOU_AUTHENTICATE_AS',
    account = 'SNOWFLAKE_ACCOUNT_IDENTIFIER',
    warehouse = 'WAREHOUSE_NAME_TO_USE',
    database = 'DATABASE_NAME_TO_USE',
    schema = 'SCHEMA_TO_USE',
    role = 'SNOWFLAKE_ROLE_TO_OPERATE_UNDER'
)

cs = conn.cursor()
cs.execute('CREATE TABLE "my_test_table" ("Column1_Name" DATATYPE ,"Column2_Name" DATATYPE)')
df = pd.read_csv(r'C:\Users\AndrewJacob78282323\Csv_File_Name.csv',sep = ',')
write_pandas(conn,df,table_name='my_test_table')
cs.close()
conn.close()

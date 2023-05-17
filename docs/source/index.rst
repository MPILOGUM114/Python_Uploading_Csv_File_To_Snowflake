UPLOADING A CSV FILE TO SNOWFLAKE WITH PYTHON
=============================================
The File Below will take you through all the steps you need to follow to upload a csv file to snowflake using the python proramming language.

Step 1 : Installation
---------------------

 **A) Download Python On Your Local Machine Using The Python Installer :** 

 `Python Installer <https://www.python.org/downloads/>`_

To Chech If Python Has Been Successfully Installed type this line on the terminal
 ``python --version``
 
 
 **B) Download snowflake-connector-python[pandas] :**
 
 In The Terminal Of Your Local Machine Type This Command To Install snowflake-connector-python[pandas] 
 
 ``pip install snowflake-connector-python[pandas]``
 

*This Library Is Used To Allow Us To Write Pandas Dataframes As Csv Files To Snowflake Tables*


**C) Install the snowflake Connector For Python In The terminal :**

``pip install --upgrade snowflake-connector-python``

 *The Snowflake Connector allows us to execute commands on snowflake via our chosen python coding platform.*
 

Step 2 : Import The Downloaded Modules On Your Coding Environment
--------------------------------------------------------------------------------

.. code-block::
    
     import snowflake.connector
     from snowflake.connector.pandas_tools import write_pandas
     import pandas as pd
     


Now We Can Utilize The Downloaded Libraries On Our IDEs Using the *Import* Keyword




Step 3: Create The Connection Between Your Snowflake Account And Your IDE  On Your Local Machine
------------------------------------------------------------------------------------------------

``conn = snowflake.connector.connect(``

``user = "USERNAME",``

``password = "PASSWORD",``

``account = "ACCOUNT_IDENTIFIER",``

``warehouse = "WAREHOUSE_NAME",``

``database = "DATABASE_NAME",``

``schema = "SCHEMA_NAME",``

``role = "ROLE_NAME"``

``)``




The Line Below Initialized The Connection To Snowflake :


``conn = snowflake.connector.connect``


The Parameters Required To Start Your Connection Include:

user - (Your Account Username)

password  - (The Password You Use To Authenticate Yourself On Snowflake)

account - (This Is Your Snowflake  Account Identifier )

warehouse - (The Name Of The  Warehouse You Will Be Working With)

database - (The Name Of The Database You Will Be Creating Your Table In)

schema - (The Schema Name You Will Be Operating Under)

role - (The User Role You Will Be Operating As)



Step 4 : Create A Cursor Object To Execute Your Query And Fetch The Results 
------------------------------------------------------------------------------

``cs = conn.cursor()``

In The Line Of Code Above, We Created A cursor object and stored It In A Variable Called cs.
The Cursor() method essentially allows us to execute queries and fetch records.


Step 5 : Create The Table To Upload The Csv File In
----------------------------------------------------

``cs.execute('CREATE TABLE "my_test_table" ("column1" VARCHAR PRIMARY KEY,"column2" VARCHAR)')``

**Note :**

*The Line Of Code Above Creates A Table Called my_test_table with 2 columns called column1 and column2 both being varchars and column1 as the primary key column*


Step 5 : Read The Csv File Into A Pandas Dataframe 
-----------------------------------------------------

``df = pd.read_csv(r'My_Csv_File.csv',sep = ',')``

This Line Of Code Above Reads A Csv File Called My_Csv_File Into A Dataframe Called Df With The Seperator set as as comma


Step 6 : Load The DataFrame Into The Table Created In Snowflake 
---------------------------------------------------------------

``write_pandas(conn,df,table_name='my_test_table')``


The *write_pandas()* function is used to write dataframes to snowflake.

conn is the connection created, df is the dataframe containing csv file and the table_name parameter sets the table name


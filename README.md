## Exercise Instructions

This is a bootstrap project to load interesting data from a Stack Exchange dataset into a data warehouse.
You are free to change anything about this bootstrap solution as you see fit, so long as it can still be executed by a reviewer.

- The project is set up to use Pipenv & Python 3.8
- SQLite3 provides an infrastructure-free simple data warehouse stand-in
- Facilites for linting etc. are provided as scripts and integrated with Pipenv

[scripts/fetch_data.sh](scripts/fetch_data.sh) is provided to download and decompress the dataset.

Your task is to make the Posts and Tags content available in an SQLite3 database.
[src/main.py](src/main.py) is provided as an entrypoint, and has an example of parsing the source data.
[src/db.py](src/db.py) is empty, but the associated test demonstrates interaction with an SQLite3 database.
You should ensure your code is correctly formatted and lints cleanly.

You will aim to make it convenient for data scientists to execute analytics-style queries reliably over the Posts and Tags tables.
You will be asked to demonstrate the solution, including:
- how you met the data scientist needs
- how you did (or would) ensure data quality
- what would need to change for the solution scale to work with a 10TB dataset with new data arriving each day

## Your Writeup!

The given excercise is finished in three tier approach
    Loading data from source (xml) files into staging tables
    Moving data from staging area to main tables
    Presentation layer to derive metrics useful for Data Sceintists /  Data Analysts using views

As a first step the solution creates the sqlite3 database and below database objects
    tbl_Stg_Posts --> staging table to store posts data
    tbl_Stg_Tags --> staging table to store tags data
    tbl_Posts --> Main table to store posts data with Id as primary key
    tbl_Tags --> Main table to store tags data with Id as the primary key
    vw_Metrics_By_Owner --> View which give the aggreagted details of Posts, Score and Viewa and Owner level
    vw_Metrics_By_Owner --> View which give the aggreagted details of Posts, Score and Viewa and ContentLicense level
PS: 
Currently the sqlite3 database is called as StackOverFlow.db, but this can be passed as parameter
More presentation layer views can be created which serves Data Acientists and Data Analysts

The database objects can be created by calling the python script as below
python .\src\create_db_objects.py  

Data pipeline:
In the first step data read from the source files (presented in Source_Files) are loaded into tbl_Stg_Posts and tbl_Stg_Tags tables respectively
In the second step data from tbl_Stg_Posts and tbl_Stg_Tags is merged with tbl_Posts and tbl_Tags respectively (Data for the existiong Ids will be updated and Data for new Ids will be inserted)
Finally data will be refreshed in the presentation layer views as soon as the data isrefreshed in the main tables

Executing the below command runs the data pipeline
python .\src\main.py

Running the test:
Executing below python script will create a test database with staging and main tables for testing and populates the tables with the test files presented in Test_Files directory
python .\src\main_test.py

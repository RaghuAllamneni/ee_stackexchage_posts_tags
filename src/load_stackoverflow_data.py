import create_db_connection
import load_staging_db
import load_main_db
from sqlite3 import Error

def load_stackoverflow():
    try:

        database = "../db/StackOverflow.db"
        conn = create_db_connection.create_connection(database)

        if conn is not None:         
            print('\n'+ 'Loading data into Stg_Posts from source xml file')
            Posts_Record_Count = load_staging_db.load_stg_posts(conn, '../Source_Files/Posts.xml')
            print('Finished loading data into Stg_Posts from source xml file')
            print('Number of records data into Stg_Posts from source xml file = '+str(Posts_Record_Count)+'\n')
            print('Loading data into Stg_Tags from source xml file')
            Tags_Record_Count = load_staging_db.load_stg_tags(conn, '../Source_Files/Tags.xml')
            print('Finished loading data into Stg_Tags from source xml file')        
            print('Number of records data into Stg_Tags from source xml file = '+str(Tags_Record_Count)+'\n')
        
        else:
            print("Error! cannot create the database connection.")

        if conn is not None: 
            print('Loading data from Stg_Posts into Posts \n')
            load_main_db.load_posts(conn)
            print('Finished loading data from Stg_Posts into Posts \n')
            print('Loading data from Stg_Tags into Tags \n')
            load_main_db.load_tags(conn)        
            print('Finished loading data from Stg_Tags into Tags \n')
        
        else:
            print("Error! cannot create the database connection.")

    except Error as error_message:
        print(error_message)

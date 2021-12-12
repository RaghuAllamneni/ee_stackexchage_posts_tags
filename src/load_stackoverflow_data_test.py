import create_db_connection
import load_staging_db_test
import load_main_db_test
import create_db_objects_test

def load_stackoverflow():
    database = "../db/StackOverflow_Test.db"
    conn = create_db_connection.create_connection(database)

    if conn is not None:         
        print('\n'+ 'Loading data into Stg_Posts from source xml file')
        load_staging_db_test.load_stg_posts(conn, '../Test_Files/Test_Posts.xml')
        print('Finished loading data into Stg_Posts from source xml file')
        print('Loading data into Stg_Tags from source xml file')
        load_staging_db_test.load_stg_tags(conn, '../Test_Files/Test_Tags.xml')
        print('Finished loading data into Stg_Tags from source xml file')        
        
    else:
        print("Error! cannot create the database connection.")

    if conn is not None: 
        print('Loading data from Stg_Posts into Posts \n')
        load_main_db_test.load_posts(conn)
        print('Finished loading data from Stg_Posts into Posts \n')
        print('Loading data from Stg_Tags into Tags \n')
        load_main_db_test.load_tags(conn)        
        print('Finished loading data from Stg_Tags into Tags \n')
    
    else:
        print("Error! cannot create the database connection.")

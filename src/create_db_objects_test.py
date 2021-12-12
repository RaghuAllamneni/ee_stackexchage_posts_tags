from sqlite3 import Error
import create_db_connection

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """       
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    
    conn.commit()
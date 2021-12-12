#from os import name
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

if __name__ == "__main__":
    database = "../db/StackOverflow.db"
    conn = create_db_connection.create_connection(database)
    sql_create_stg_posts_table = """ CREATE TABLE IF NOT EXISTS tbl_Stg_Posts (
            Id text,
            PostTypeId text,
            ParentId text,
            AcceptedAnswerId text,
            CreationDate text,
            Score text,
            ViewCount text,
            Body text,
            OwnerUserId text,
            LastEditorUserId text,
            LastEditDate text,
            LastActivityDate text,
            Title text,
            Tags text,
            AnswerCount text,
            CommentCount text,
            FavouriteCount text,
            ContentLicence text
        ); """

    sql_create_stg_tags_table = """CREATE TABLE IF NOT EXISTS tbl_Stg_Tags (
                                    Id text,
                                    TagName text,
                                    Count text,
                                    ExcerptPostId text,
                                    WikiPostId text
                                );"""

    sql_create_posts_table = """ CREATE TABLE IF NOT EXISTS tbl_Posts (
            Id text PRIMARY KEY,
            PostTypeId text,
            ParentId text,
            AcceptedAnswerId text,
            CreationDate text,
            Score text,
            ViewCount text,
            Body text,
            OwnerUserId text,
            LastEditorUserId text,
            LastEditDate text,
            LastActivityDate text,
            Title text,
            Tags text,
            AnswerCount text,
            CommentCount text,
            FavouriteCount text,
            ContentLicence text,
            DbInsertDate text DEFAULT (datetime('now')),
            DbUpdateDate text DEFAULT (datetime('now'))
        ); """

    sql_create_tags_table = """CREATE TABLE IF NOT EXISTS tbl_Tags (
                                    Id text PRIMARY KEY,
                                    TagName text,
                                    Count text,
                                    ExcerptPostId text,
                                    WikiPostId text,
                                    DbInsertDate text DEFAULT (datetime('now')),
                                    DbUpdateDate text DEFAULT (datetime('now'))
                                );"""

    sql_create_view_metrics__by_owner = """ CREATE VIEW IF NOT EXISTS vw_Metrics_By_Owner AS
                                        SELECT OwnerUserId, COUNT(Id) AS Number_Of_Posts, SUM(Score) Total_Score, SUM(ViewCount) Total_Views FROM tbl_Posts
                                        GROUP BY OwnerUserId
                                        HAVING Number_Of_Posts >= 10;"""

    sql_create_view_metrics__by_license = """ CREATE VIEW IF NOT EXISTS vw_Metrics_By_License AS
                                        SELECT ContentLicence, COUNT(Id) AS Number_Of_Posts, SUM(Score) Total_Score, SUM(ViewCount) Total_Views FROM tbl_Posts
                                        GROUP BY ContentLicence
                                        HAVING Number_Of_Posts >= 10;"""

    print('Creating staging table --> stg_posts')

    create_table(conn, sql_create_stg_posts_table)

    print('Created staging table --> stg_posts \n')
    print('Creating staging table --> stg_tags')

    create_table(conn, sql_create_stg_tags_table)

    print('Created staging table --> stg_tags \n')
    print('Creating main table --> posts')

    create_table(conn, sql_create_posts_table)

    print('Created main table --> posts \n')
    print('Creating main table --> posts')

    create_table(conn, sql_create_tags_table)

    print('Created main table --> posts \n')
    print('Creating View to get Metrics by owner Id --> vw_Metrics_By_Owner')

    create_table(conn, sql_create_view_metrics__by_owner)

    print('Created View to get Metrics by owner Id --> vw_Metrics_By_Owner \n')
    print('Creating View to get Metrics by License --> vw_Metrics_By_License')
    
    create_table(conn, sql_create_view_metrics__by_license)

    print('Created View to get Metrics by License --> vw_Metrics_By_License \n')

import load_stackoverflow_data_test
import create_db_connection
import create_db_objects_test

if __name__ == '__main__':
    database = "./db/StackOverflow_Test.db"
    conn = create_db_connection.create_connection(database)
    sql_create_stg_posts_table = """ CREATE TABLE IF NOT EXISTS tbl_Stg_Posts_Test (
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

    sql_create_stg_tags_table = """CREATE TABLE IF NOT EXISTS tbl_Stg_Tags_Test (
                                    Id text,
                                    TagName text,
                                    Count text,
                                    ExcerptPostId text,
                                    WikiPostId text
                                );"""

    sql_create_posts_table = """ CREATE TABLE IF NOT EXISTS tbl_Posts_Test (
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
            ContentLicence text
        ); """

    sql_create_tags_table = """CREATE TABLE IF NOT EXISTS tbl_Tags_Test (
                                    Id text PRIMARY KEY,
                                    TagName text,
                                    Count text,
                                    ExcerptPostId text,
                                    WikiPostId text
                                );"""

    
    create_db_objects_test.create_table(conn, sql_create_stg_posts_table)
    create_db_objects_test.create_table(conn, sql_create_stg_tags_table)
    create_db_objects_test.create_table(conn, sql_create_posts_table)
    create_db_objects_test.create_table(conn, sql_create_tags_table)

           
    load_stackoverflow_data_test.load_stackoverflow()

    cursor = conn.cursor()

    assert list(cursor.execute("SELECT * FROM tbl_stg_posts_test;")
           )  == [('1', '2', '3', '4', '2021-12-12', '5', '6', '7', '8', '9', '2021-12-12', '1900-01-01', '10', '11', '12', '13', '14', '15')]

    assert list(cursor.execute("SELECT * FROM tbl_stg_tags_test;")
           )  == [('1', 'tag1', '99', '12345', '6789')]


    assert list(cursor.execute("SELECT * FROM tbl_posts_test;")
           )  == [('1', '2', '3', '4', '2021-12-12', '5', '6', '7', '8', '9', '2021-12-12', '1900-01-01', '10', '11', '12', '13', '14', '15')]

    assert list(cursor.execute("SELECT * FROM tbl_tags_test;")
           )  == [('1', 'tag1', '99', '12345', '6789')]
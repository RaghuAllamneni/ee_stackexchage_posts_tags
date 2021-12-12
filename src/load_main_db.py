import sqlite3

def load_posts(conn):
        
    cur = conn.cursor()

    cur.execute("INSERT OR REPLACE INTO tbl_Posts (Id, PostTypeId, ParentId, AcceptedAnswerId, CreationDate, Score, ViewCount \
                    , Body, OwnerUserId, LastEditorUserId, LastEditDate, LastActivityDate \
                    , Title, Tags, AnswerCount, CommentCount, FavouriteCount, ContentLicence) \
                    SELECT * FROM tbl_Stg_Posts;")

    conn.commit()

def load_tags(conn):
    cur = conn.cursor()

    cur.execute("INSERT OR REPLACE INTO tbl_Tags (Id, TagName, Count, ExcerptPostId, WikiPostId) \
                      SELECT * FROM tbl_Stg_Tags;")

    conn.commit()

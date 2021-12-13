from sqlite3.dbapi2 import Error
import xml.etree.ElementTree as ET

def load_stg_posts(conn, srcfile):

    postsTree = ET.ElementTree(file=srcfile)
    postsRoot = postsTree.getroot()
    Posts = []
    for tag in postsRoot:
        Id = tag.get('Id')
        PostTypeId = tag.get('PostTypeId')
        ParentId = tag.get('ParentId')
        AcceptedAnswerId = tag.get('AcceptedAnswerId')
        CreationDate = tag.get('CreationDate')
        Score = tag.get('Score')
        ViewCount = tag.get('ViewCount')
        Body = tag.get('Body')
        OwnerUserId = tag.get('OwnerUserId')
        LastEditorUserId = tag.get('LastEditorUserId')
        LastEditDate = tag.get('LastEditDate')
        LastActivityDate = tag.get('LastActivityDate')
        Title = tag.get('Title')
        Tags = tag.get('Tags')
        AnswerCount = tag.get('AnswerCount')
        CommentCount = tag.get('CommentCount')
        FavoriteCount = tag.get('FavoriteCount')
        ContentLicence = tag.get('ContentLicense')
        Posts.append((Id, PostTypeId, ParentId, AcceptedAnswerId, CreationDate, Score, ViewCount
                    , Body, OwnerUserId, LastEditorUserId, LastEditDate, LastActivityDate
                    , Title, Tags, AnswerCount, CommentCount, FavoriteCount, ContentLicence))
        
    cur = conn.cursor()

    cur.execute("DELETE FROM tbl_Stg_Posts")
    cur.executemany("INSERT INTO tbl_Stg_Posts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", Posts)

    conn.commit()

    cur.execute("SELECT COUNT(1) FROM tbl_Stg_Posts;")
    record_count = cur.fetchall()
    for records_loaded in record_count:
        return str(records_loaded[0])

def load_stg_tags(conn, srcfile):

    tagsTree = ET.ElementTree(file=srcfile)
    tagsRoot = tagsTree.getroot()
    tags = []
    for tag in tagsRoot:
        Id = tag.get('Id')
        TagName = tag.get('TagName')
        Count = tag.get('Count')
        ExcerptPostId = tag.get('ExcerptPostId')
        WikiPostId = tag.get('WikiPostId')
        tags.append((Id, TagName, Count, ExcerptPostId, WikiPostId))

    cur = conn.cursor()

    cur.execute("DELETE FROM tbl_Stg_Tags")
    cur.executemany("INSERT INTO tbl_Stg_Tags VALUES (?, ?, ?, ?, ?)", tags)

    conn.commit()

    cur.execute("SELECT COUNT(1) FROM tbl_Stg_Tags;")
    record_count = cur.fetchall()
    for records_loaded in record_count:
        return str(records_loaded[0])
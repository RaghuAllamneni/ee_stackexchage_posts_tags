import xml.etree.ElementTree as ET

def load_stg_posts(conn, srcfile):
    myTree = ET.ElementTree(file=srcfile)
    myRoot = myTree.getroot()
    Posts = []
    for tag in myRoot:
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
   
    cur.execute("DELETE FROM tbl_Stg_Posts_Test")
    cur.executemany("INSERT INTO tbl_Stg_Posts_Test VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", Posts)

    conn.commit()

def load_stg_tags(conn, srcfile):
    myTree = ET.ElementTree(file=srcfile)
    myRoot = myTree.getroot()
    tags = []
    for tag in myRoot:
        Id = tag.get('Id')
        TagName = tag.get('TagName')
        Count = tag.get('Count')
        ExcerptPostId = tag.get('ExcerptPostId')
        WikiPostId = tag.get('WikiPostId')
        tags.append((Id, TagName, Count, ExcerptPostId, WikiPostId))

    cur = conn.cursor()

    cur.execute("DELETE FROM tbl_Stg_Tags_Test")
    cur.executemany("INSERT INTO tbl_Stg_Tags_Test VALUES (?, ?, ?, ?, ?)", tags)

    conn.commit()

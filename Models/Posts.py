import Models.Provider as Provider
from flask_sqlalchemy import SQLAlchemy


# Admin - Post
def Insert_Post(content,dateCreate):
    query = "INSERT INTO Posts ('content','dateCreate') VALUES ('{}','{}')".format(content,dateCreate)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Update_Post(idPost,content,dateCreate):
    query = "UPDATE Posts SET content='{}', dateCreate='{}' WHERE idPost={}".format(content,dateCreate,idPost)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Delete_Post(idPost):
    query = "DELETE FROM Posts WHERE idPost={}".format(idPost)
    msg = Provider.ExecuteNonQuery(query)
    return msg


# Test 
# Insert_Post('Good','2010-10-10')
# Update_Post(1,'Yeh','01-09-2002')
# Delete_Post(1)
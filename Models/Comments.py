import Provider as Provider

from flask_sqlalchemy import SQLAlchemy


# Admin - Post
def Insert_Comment(content,dateCreate,idUser,ranked):
    query = "INSERT INTO Comments ('content','dateCreate',idUser,ranked) VALUES ('{}','{}','{}','{}')".format(content,dateCreate,idUser,ranked)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Update_Comment(content,ranked,idComment):
    query = "UPDATE Comments SET content='{}',ranked={} WHERE idComment={}".format(content,ranked,idComment)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Delete_Comment(idComment):
    query = "DELETE FROM Comments WHERE idComment={}".format(idComment)
    msg = Provider.ExecuteNonQuery(query)
    return msg


def Get_Comment():
    query = "SELECT * FROM Comment"

    try : 
        record = Provider.ExecuteQuery(query)
        return record

    except:
        return None

    
# Test 

# Insert_Comment('sadsa','2010-10-10',1,1)

Update_Comment('Yesadsadah',10,2)
Delete_Comment(2)
Get_Comment()
















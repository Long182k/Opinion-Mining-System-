import Models.Provider as Provider

from flask_sqlalchemy import SQLAlchemy


# Admin - Post
def Insert_Comment(content,dateCreate,ranked,idUser,idPost):
    query = "INSERT INTO Comments ('content','dateCreate',ranked,idUser,idPost) VALUES ('{}','{}','{}','{}','{}')".format(content,dateCreate,ranked,idUser,idPost)
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
    query = "SELECT * FROM Comments"

    try : 
        record = Provider.ExecuteQuery(query)
        return record

    except:
        return None

    
# Test 

# Insert_Comment('sadsa','2010-10-10',1,1)

Update_Comment('Yesadsadah',10,2)
# Delete_Comment(2)
# Get_Comment()

#
# def SentimentAnalysisProcess(self,tweet,positivelist,negativelist):
#     ps = PorterStemmer()
#     # PorterStemmer using for look up words have 1 root word
#     # For example : Root Word : Like include Likes Liking Liked Likely
#
#     tweet = word_tokenize(tweet)
#     tweet_list = []
#     score = 0
#
#     for word in tweet:
#         word = ps.stem(word)
#         if word in positivelist:
#             score += score
#
#         elif word in negativelist:
#             score -= score
#
#         else:
#             pass
#     return score
#
# def checkRank(self,score,rank):
#     query = "SELECT ranked FROM Comments"
#     rank = Provider.ExecuteQuery(query)
#     if (score > 0):
#         rank = "Good"
#     elif (score == 0):
#         rank = "Neutral"
#     else:
#         rank = "Bad"
#     return rank
#
#
#














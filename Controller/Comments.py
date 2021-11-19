from flask import request, jsonify, json

from init import app

from Models import Comments
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

@app.route('/api/create_comment', methods=['POST'])
def create_comment():
    json_data = request.json

    content = json_data['content']
    dateCreate = json_data ['dateCreate']
    ranked = json_data['ranked']
    idUser = json_data['idUser']
    idPost = json_data['idPost']

    try:
        status = Comments.Insert_Comment(content,dateCreate,ranked,idUser,idPost)
    except:
        status = 'The Comment is already post'
    return jsonify({'result':status})
    

    
@app.route('/api/get_comment', methods = ['GET'])
def get_comment():


    get_comment = Comments.Get_Comment()

    try:
        CommentList = []

        for i in get_comment:
            cmtDict = {
            'idComment': i[0],    
            'idPost': i[1],
            'idUser': i[2],
            'content': i[3],
            'dateCreate': i[4],
            'ranked': i[5]
            }
            CommentList.append(cmtDict)
        
            # convert to json data
            jsonStr = json.dumps(CommentList)
 
    except Exception as e:
        print(e)

    return jsonify(jsonStr)



@app.route('/api/update_comment', methods = ['PUT'])
def update_comment():
    
    json_data = request.json

    update_comment = Comments.Update_Comment(json_data['content'],json_data['ranked'],json_data['idComment'])

    return jsonify({'result':update_comment})



@app.route('/api/delete_comment/<idComment>', methods = ['DELETE'])
def delete_comment(idComment):

    delete_comment = Comments.Delete_Comment(idComment)

    return jsonify({'result':delete_comment})


        

def SentimentAnalysisProcess(content,):
    ps = PorterStemmer()
    # PorterStemmer using for look up words have 1 root word
    # For example : Root Word : Like include Likes Liking Liked Likely

    tweet = word_tokenize(content)
    tweet_list = []
    score = 0

    for word in tweet:
        word = ps.stem(word)
        if word in positivelist:
            score += score

        elif word in negativelist:
            score -= score

        else:
            pass
    return score

def checkRank(self,score,rank):
    query = "SELECT ranked FROM Comments"
    rank = Provider.ExecuteQuery(query)
    if (score > 0):
        rank = "Good"
    elif (score == 0):
        rank = "Neutral"
    else:
        rank = "Bad"
    return rank
    


#






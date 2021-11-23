from flask import request, jsonify, json
from flask_cors import cross_origin
from nltk.tokenize import word_tokenize

from init import app

from Models import Admin
from Models import Comments
from Models import Keywords

@app.route('/api/ad_create_keyword', methods=['POST'])
@cross_origin()
def ad_create_keyword():
    json_data = request.json

    category = json_data['category']
    content = json_data['content']
    score = json_data['score']

    try:
        status = Admin.Admin_InsertKeyword(category,content,score)
    except:  
        status = 'The Admin Insert Keyword successfully'
    return jsonify({'result':status})


@app.route('/api/ad_get_keyword', methods = ['GET'])
@cross_origin()
def ad_get_keyword():

    ad_get_keyword = Admin.AdminGetKeyword()

    try:
        KeywordList = []

        for i in ad_get_keyword:
            KeywordDict = {
            'idKeyword': i[0],
            'category': i[1],
            'score': i[2],
            'content': i[3],
            }
            KeywordList.append(KeywordDict)
        
            # convert to json data
            jsonStr = json.dumps(KeywordList)

    except Exception as e:
        print(e)

    return jsonify(jsonStr)

def TinhLaiToanBoKeyword():
    score = 0 

    '''
        LISTKEYWORD:
            0 - idKeyword
            1 - category
            2 - score
            3 - content
    '''
    ListKeyword = Keywords.GetKeyword()
    
    '''
        ALLCMT:
            0 - idComment
            1 - idPost
            2 - idUser
            3 - content
            4 - dateCreate
            5 - ranked
    '''
    AllCmt = Comments.Get_Comment()
    
    for cmt in AllCmt:
        Listword = word_tokenize(cmt[3])

        for word in Listword:
            for keyword in ListKeyword:
                if word == keyword[3]:
                    score = score + keyword[2]
                    break
        
        ranked = 'GOOD' if score > 0 else 'BAD'
        status = Comments.Update_Comment(cmt[3], ranked, cmt[0])
        print(status + '\n')

@app.route('/api/ad_update_keyword', methods = ['PUT'])
@cross_origin()
def ad_update_keyword():
    
    json_data = request.json

    ad_update_keyword = Admin.Admin_UpdateKeyword(json_data['category'],json_data['content'],json_data['score'],json_data['idKeyword'])
    TinhLaiToanBoKeyword()
    return jsonify({'result':ad_update_keyword})


@app.route('/api/ad_delete_keyword/<idKeyword>', methods = ['DELETE'])
@cross_origin()
def ad_delete_keyword(idKeyword):

    ad_delete_keyword = Admin.Admin_DeleteKeyword(idKeyword)

    return jsonify({'result':ad_delete_keyword})

    
        







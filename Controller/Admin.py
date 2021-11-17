from flask import request, jsonify, json

from init import app

from Models import Admin

@app.route('/api/ad_create_keyword', methods=['POST'])
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

@app.route('/api/ad_update_keyword', methods = ['PUT'])
def ad_update_keyword():
    
    json_data = request.json

    ad_update_keyword =Admin.Admin_UpdateKeyword(json_data['category'],json_data['content'],json_data['score'],json_data['idKeyword'])

    return jsonify({'result':ad_update_keyword})


@app.route('/api/ad_delete_keyword/<idKeyword>', methods = ['DELETE'])
def ad_delete_keyword(idKeyword):

    ad_delete_keyword = Admin.Admin_DeleteKeyword(idKeyword)

    return jsonify({'result':ad_delete_keyword})

    
        







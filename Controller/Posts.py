from flask import request, jsonify, json

from init import app

from Models import Posts

@app.route('/api/create_post', methods=['POST'])
def create_post():
    json_data = request.json

    content = json_data['content']
    dateCreate = json_data ['dateCreate']
    idUser = json_data['idUser']
    
    try:
        status = Posts.Insert_Post(content,dateCreate,idUser)
    except:
        status = 'The Post is already post'
    return jsonify({'result':status})
    

    
@app.route('/api/get_post', methods = ['GET'])
def get_post():


    get_post = Posts.GetPost()

    try:
        PostList = []

        for i in get_post:
            postDict = {
            'idPost': i[0],
            'content': i[1],
            'dateCreate': i[2],
            'idUser': i[3],
            }
            PostList.append(postDict)
        
            # convert to json data
            jsonStr = json.dumps(PostList)

    except Exception as e:
        print(e)

    return jsonify(jsonStr)



@app.route('/api/update_post', methods = ['PUT'])
def update_post():
    
    json_data = request.json

    update_post = Posts.Update_Post(json_data['idPost'],json_data['content'])

    return update_post


@app.route('/api/delete_post/<idPost>', methods = ['DELETE'])
def delete_post(idPost):

    delete_post = Posts.Delete_Post(idPost)

    return jsonify({'result':delete_post})

    
        







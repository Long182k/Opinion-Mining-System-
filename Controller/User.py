from flask import request, jsonify, json
from nltk.tokenize import word_tokenize

from init import app

from Models import Comments
from Models import Keywords
from Models import Posts
from Models import Images


def TinhDiemCmt(content,dateCreate,ranked,idUser,idPost):

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
    
    Listword = word_tokenize(content)

    for word in Listword:
        for keyword in ListKeyword:
            if word == keyword[3]:
                score = score + keyword[2]
                break
        
    ranked = 'GOOD' if score > 0 else 'BAD'
    status = Comments.Insert_Comment(content,dateCreate,ranked,idUser,idPost)

    return status
'''
    User 1: cmt vô post đó là ABC
    User 2: cmt vô tiếp thì gọi create trước [lúc này trên client vẫn chỉ có cmt của User 1]
            sau khi create trong db nó 2 cmt của bài post đó nhưng client vẫn 1
            lúc này mình gọi lại 1 hàm get thì nó mới lấy được cả 2 cmt rồi trả lên show lại
'''

@app.route('/api/user_create_cmt', methods=['POST'])
def user_create_cmt():
    json_data = request.json

    
    content = json_data['content']
    dateCreate = json_data['dateCreate']
    ranked = json_data['ranked']
    idUser = json_data['idUser']
    idPost = json_data['idPost']
    
    try:
        status = TinhDiemCmt(content)
    except:  
        status = 'The Comment has already execute.'
    return jsonify({'result':status})

# # def TinhDiemCmt(content,dateCreate,ranked,idUser,idPost):
# def TinhDiemCmt():

#     score = 0 
 
#     '''
#         LISTKEYWORD:
#             0 - idKeyword
#             1 - category
#             2 - score
#             3 - content
#     '''
    
#     ListKeyword = Keywords.GetKeyword()
    
#     '''
#         ALLCMT:
#             0 - idComment
#             1 - idPost
#             2 - idUser
#             3 - content
#             4 - dateCreate
#             5 - ranked
#     '''
#     AllCmt = Comments.Get_Comment()
    

#     for cmt in AllCmt:
#         Listword = word_tokenize(cmt[3])
#         for word in Listword:
#             for keyword in ListKeyword:
#                 if word == keyword[3]:
#                     score = score + keyword[2]
#                     break
        
#         ranked = 'GOOD' if score > 0 else 'BAD'
#         status = Comments.Insert_Comment(cmt[1],cmt[2],cmt[3],cmt[4],ranked)
#         # status = Comments.Insert_Comment(content,dateCreate,ranked,idUser,idPost)

#         return status
# '''
#     User 1: cmt vô post đó là ABC
#     User 2: cmt vô tiếp thì gọi create trước [lúc này trên client vẫn chỉ có cmt của User 1]
#             sau khi create trong db nó 2 cmt của bài post đó nhưng client vẫn 1
#             lúc này mình gọi lại 1 hàm get thì nó mới lấy được cả 2 cmt rồi trả lên show lại
# '''

# @app.route('/api/user_create_cmt', methods=['POST'])
# def user_create_cmt():
#     json_data = request.json

    
#     content = json_data['content']
#     dateCreate = json_data['dateCreate']
#     ranked = json_data['ranked']
#     idUser = json_data['idUser']
#     idPost = json_data['idPost']
    
#     try:
#         status = Comments.Insert_Comment(content,dateCreate,ranked,idUser,idPost)
#         TinhDiemCmt(content,ranked)
#     except:  
#         status = 'The Comment has already execute.'
#     return jsonify({'result':status})


@app.route('/api/get_comment', methods = ['GET'])

def get_comment():


    comments = Comments.Get_Comment()

    try:
        CommentList = []

        for i in comments:
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


    posts = Posts.GetPost()

    try:
        PostList = []

        for i in posts:
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

    return jsonify({'result':update_post})



@app.route('/api/delete_post/<idPost>', methods = ['DELETE'])
def delete_post(idPost):

    delete_post = Posts.Delete_Post(idPost)

    return jsonify({'result':delete_post})

    
        
@app.route('/api/create_image', methods=['POST'])
def create_image():
    json_data = request.json

    idPost = json_data['idPost']
    path = json_data ['path']
    
    try:
        status = Images.Insert_Image(idPost,path)
    except:
        status = 'The Image is already post'
    return jsonify({'result':status})
    

    
@app.route('/api/get_image', methods = ['GET'])
def get_image():


    images = Images.Get_Image()

    try:
        ImageList = []

        for i in images:
            imageDict = {
            'idImage': i[0],
            'idPost': i[1],
            'path': i[2],
            }
            ImageList.append(imageDict)
        
            # convert to json data
            jsonStr = json.dumps(ImageList)

    except Exception as e:
        print(e)

    return jsonify(jsonStr)



@app.route('/api/update_image', methods = ['PUT'])
def update_image():
    
    json_data = request.json

    update_image = Images.Update_Image(json_data['path'],json_data['idImage'])
    
    return jsonify({'result':update_image})




@app.route('/api/delete_image/<idImage>', methods = ['DELETE'])
def delete_image(idImage):

    delete_image = Images.Delete_Image(idImage)

    return jsonify({'result':delete_image})

    
        
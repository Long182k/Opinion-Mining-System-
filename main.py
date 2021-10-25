import Models.Admin
import Models.Keywords
import Models.Posts
from flask import Flask



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sent_al.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)


app.run(host='localhost', port=5000,debug = True, threaded = True, use_reloader = False)

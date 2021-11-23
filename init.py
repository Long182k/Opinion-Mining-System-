from flask import Flask
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)
# cors = CORS(app)
api = Api(app)

CORS(app, origins="http://localhost:5500", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DEL ETE,OPTIONS')
  return response


app.config['CORS_HEADERS'] = 'Content-Type'

app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sent_al.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


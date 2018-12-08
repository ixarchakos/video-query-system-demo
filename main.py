from datetime import timedelta, datetime
from flask import Flask, render_template, request, session, redirect, url_for, jsonify, flash
from flask_socketio import SocketIO,emit, join_room
from json import loads
import os, time
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

app = Flask(__name__)

socketio = SocketIO(app)
# @app.route("/getimagecomments", methods=['POST'])
# def getimagecomments():
#     image_id = request.json['imageId']
#     resultset = get_image_comments(image_id)
#     return jsonify({"result": resultset})


# @app.route("/addcomment", methods=['POST'])
# def addcomment():
#     image_id = request.json['imageId']
#     if 'user_id' in session:
#         uid = session["user_id"]
#     else:
#         uid = ""
#     comment = request.json['comment']
#     resultset = add_comment(uid,image_id,comment)
#     return jsonify({"result": resultset})

@app.route("/get_image_prediction", methods=['POST'])
def get_image_prediction(dataset):
	region = request.json['region']
	# image_list = os.listdir(ROOT_DIR + '/static/images/' + request.json['dataset'])
	image_list = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'll', 'ww']
	for i in image_list:
		print(i)
	# jsonify({"result": {'value':i}})
	

@app.route("/index")
@app.route("/", methods=["GET"])
def index():
	
    return render_template("home.html")

if __name__ == '__main__':
	socketio.run(app, port=5008, debug=True)

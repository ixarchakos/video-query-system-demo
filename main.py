from datetime import timedelta, datetime
from flask import Flask, render_template, request, session, redirect, url_for, jsonify, flash
from flask_socketio import SocketIO,emit, join_room
from json import loads
import os, time

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

socketio = SocketIO(app)


@app.route("/get_image_prediction", methods=['POST'])
def get_image_prediction():
	count = request.json['count']
	image_list = sorted(os.listdir(ROOT_DIR + '/static/images/' + 'detrac'))
	return jsonify({"result": {'value':image_list[count], 'prediction': False}})
	

@app.route("/index")
@app.route("/", methods=["GET"])
def index():
    return render_template("home.html")


if __name__ == '__main__':
	socketio.run(app, port=5008, debug=True)

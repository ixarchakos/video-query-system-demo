from datetime import timedelta, datetime
from flask import Flask, render_template, request, session, redirect, url_for, jsonify, flash
from flask_socketio import SocketIO,emit, join_room
from json import loads
import os, time

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

socketio = SocketIO(app)


@app.route("/get_accuracy", methods=['POST'])
def get_accuracy():
	input_video = request.json['input']
	interval = request.json['interval']

	label = dict()
	if input_video == 'detrac' and (interval == 300 or interval == 1001):
		with open('/home/yannis/Documents/video-query-system-demo/static/results/brute/detrac.csv', 'r') as truth:
			for t in truth:
				split = t.split(',')
				label[split[0]] = [int(split[1]), int(split[2].rstrip())]
	elif input_video == 'square' and (interval == 300 or interval == 1001):
		with open('/home/yannis/Documents/video-query-system-demo/static/results/brute/square.csv', 'r') as truth:
			for t in truth:
				split = t.split(',')
				label[split[0]] = [int(split[1]), int(split[2].rstrip())]
	elif input_video == 'square' and (interval == 0.7 or interval == 1000):
		with open('/home/yannis/Documents/video-query-system-demo/static/results/opt/square.csv', 'r') as truth:
			for t in truth:
				split = t.split(',')
				label[split[0]] = [int(split[1]), int(split[2].rstrip())]


	correct, total = 0.0, 0.0
	for l in label.values():
		if l[0] == l[1]:
			correct += 1
		total += 1

	return jsonify({"result": round((correct/total) * 100, 1)})


@app.route("/get_image_prediction", methods=['POST'])
def get_image_prediction():
	print('mpika4')
	count = request.json['count']
	input_video = request.json['input']
	interval = request.json['interval']
	label = dict()
	if input_video == 'detrac' and (interval == 300 or interval == 1001):
		with open('/home/yannis/Documents/video-query-system-demo/static/results/brute/detrac.csv', 'r') as truth:
			for t in truth:
				split = t.split(',')
				label[split[0]] = [int(split[1]), int(split[2].rstrip())]
	elif input_video == 'square' and (interval == 300 or interval == 1001):
		with open('/home/yannis/Documents/video-query-system-demo/static/results/brute/square.csv', 'r') as truth:
			for t in truth:
				split = t.split(',')
				label[split[0]] = [int(split[1]), int(split[2].rstrip())]
	elif input_video == 'square' and (interval == 0.7 or interval == 1000):
		with open('/home/yannis/Documents/video-query-system-demo/static/results/opt/square.csv', 'r') as truth:
			for t in truth:
				split = t.split(',')
				label[split[0]] = [int(split[1]), int(split[2].rstrip())]
	elif input_video == 'detrac_localisation' and (interval == 300 or interval == 1001):
		print('mpika5')
		with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/brute/yolo_results_', 'r') as truth:
			for t in truth:
				split = t.split(",")
				if split[-1].strip() == "False":
					label[split[0]] = ["1", "0"]
				elif split[-1].strip()  == "True":
					label[split[0]] = ["1", "1"]


	print(label)
	image_list = sorted(os.listdir(ROOT_DIR + '/static/images/' + input_video))
	prediction = False
	if label[image_list[count]][0] == label[image_list[count]][1]:
		prediction = True
	return jsonify({"result": {'value':image_list[count], 'prediction': prediction}})
	

@app.route("/index")
@app.route("/", methods=["GET"])
def index():
    return render_template("home.html")


if __name__ == '__main__':
	socketio.run(app, port=5009, debug=True)

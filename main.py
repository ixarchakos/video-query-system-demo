from datetime import timedelta, datetime
from flask import Flask, render_template, request, session, redirect, url_for, jsonify, flash
from flask_socketio import SocketIO,emit, join_room
from json import loads
from app.utils import get_pred_bbox, get_pred_accuracy
import os, time
import ast
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

socketio = SocketIO(app)


@app.route("/get_accuracy", methods=['POST'])
def get_accuracy():
	input_video = request.json['input']
	interval = request.json['interval']
	predicates = request.json['predicates']
	label = dict()
	if input_video == 'clip1' and (interval == 300 or interval == 1001):
		if predicates == "":
			with open('/home/yannis/Documents/video-query-system-demo/static/results/brute/yolo_results_count', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		if "car behind" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/brute/yolo_results_car_behind_car', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "car left" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/car_left_to_truck/brute/yolo_results_car_left', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "bus == 1" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/bus/brute/yolo_results_bus_count', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "car > 1" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/car/brute/yolo_results_car_count', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
	elif input_video == 'clip1' and (interval == 0.7 or interval == 1000):
		if predicates == "":
			with open('/home/yannis/Documents/video-query-system-demo/static/results/opt/opt_count', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "bus == 1" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/bus/opt/opt_bus_classcount', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "car > 1" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/car/opt/opt_car_classcount', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "car behind" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/opt/opt_car_behind_car', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "car left" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/car_left_to_truck/opt/opt_car_left_to_bus', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
	elif input_video == 'clip2' and (interval == 300 or interval == 1001):
		if "bus >= 2" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/clip2/bus/brute/yolo_results_bus_count_2_bigger2', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "car >= 3" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/clip2/car/brute/yolo_results_car_count_2_bigger3', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "bus right" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/clip2/yolo_results_bus_right_car', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "behind bus" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/clip2/yolo_car_behind_bus', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
	elif input_video == 'clip2' and (interval == 0.7 or interval == 1000):
		if "car >= 3" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/clip2/car/opt/opt_car_count_2', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "bus >= 2" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/clip2/bus/opt/opt_bus_count_2', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "bus right" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/clip2/opt_bus_right_car', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
		elif "car behind bus" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/clip2/opt_car_behind_bus', 'r') as truth:
				accuracy = get_pred_accuracy(truth)
			return jsonify({"result": round(accuracy * 100, 1)})
	
	
	correct, total = 0.0, 0.0
	for l in label.values():
		if l[0] == l[1]:
			correct += 1
		total += 1

	return jsonify({"result": round((correct/total) * 100, 1)})


@app.route("/get_image_prediction", methods=['POST'])
def get_image_prediction():
	count = request.json['count']
	input_video = request.json['input']
	interval = request.json['interval']
	predicates = request.json['predicates']
	bbox = False
	image_list = sorted(os.listdir(ROOT_DIR + '/static/images/' + input_video))
	label, bbox = dict(), dict()
	if input_video == 'clip1' and (interval == 300 or interval == 1001):
		if predicates == "":
			with open('/home/yannis/Documents/video-query-system-demo/static/results/brute/yolo_results_count', 'r') as truth:
				label = dict()
				for t in truth:
					split = t.split(",")
					if split[-1].strip() == "False":
						label[split[0]] = ["1", "0"]
					elif split[-1].strip()  == "True":
						label[split[0]] = ["1", "1"]
		if "car behind" in predicates.lower():
			print('mpika5')
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/brute/yolo_results_car_behind_car', 'r') as truth:
				label, bbox = get_pred_bbox(truth)
		elif "car left" in predicates.lower():
			print('mpika6')
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/car_left_to_truck/brute/yolo_results_car_left', 'r') as truth:
				label, bbox = get_pred_bbox(truth)
		elif "bus == 1" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/bus/brute/yolo_results_bus_count', 'r') as truth:
				label, bbox = get_pred_bbox(truth)
		elif "car > 1" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/car/brute/yolo_results_car_count', 'r') as truth:
				label, bbox = get_pred_bbox(truth)
	elif input_video == 'clip1' and (interval == 0.7 or interval == 1000):
		if predicates == "":
			with open('/home/yannis/Documents/video-query-system-demo/static/results/opt/opt_count', 'r') as truth:
				for t in truth:
					split = t.split(",")
					if split[-1].strip() == "False":
						label[split[0]] = ["1", "0"]
					elif split[-1].strip()  == "True":
						label[split[0]] = ["1", "1"]
		elif "bus == 1" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/bus/opt/opt_bus_classcount', 'r') as truth:
				for t in truth:
					split = t.split(",")
					if split[-1].strip() == "False":
						label[split[0]] = ["1", "0"]
					elif split[-1].strip()  == "True":
						label[split[0]] = ["1", "1"]
		elif "car > 1" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/car/opt/opt_car_classcount', 'r') as truth:
				for t in truth:
					split = t.split(",")
					if split[-1].strip() == "False":
						label[split[0]] = ["1", "0"]
					elif split[-1].strip()  == "True":
						label[split[0]] = ["1", "1"]
		elif "car behind" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/opt/opt_car_behind_car', 'r') as truth:
				for t in truth:
					split = t.split(",")
					if split[-1].strip() == "False":
						label[split[0]] = ["1", "0"]
					elif split[-1].strip()  == "True":
						label[split[0]] = ["1", "1"]
		elif "car left" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/car_left_to_truck/opt/opt_car_left_to_bus', 'r') as truth:
				for t in truth:
					split = t.split(",")
					if split[-1].strip() == "False":
						label[split[0]] = ["1", "0"]
					elif split[-1].strip()  == "True":
						label[split[0]] = ["1", "1"]
	elif input_video == 'clip2' and (interval == 300 or interval == 1001):
		if "bus >= 2" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/clip2/bus/brute/yolo_results_bus_count_2_bigger2', 'r') as truth:
				label, bbox = get_pred_bbox(truth)
		elif "car >= 3" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/clip2/car/brute/yolo_results_car_count_2_bigger3', 'r') as truth:
				label, bbox = get_pred_bbox(truth)
		elif "behind bus" in predicates.lower():
			print(predicates)
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/clip2/yolo_car_behind_bus', 'r') as truth:
				label, bbox = get_pred_bbox(truth)
		elif "bus right" in predicates.lower():
			print(predicates)
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/clip2/yolo_results_bus_right_car', 'r') as truth:
				label, bbox = get_pred_bbox(truth)
	elif input_video == 'clip2' and (interval == 0.7 or interval == 1000):
		if "bus >= 2" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/clip2/bus/opt/opt_bus_count_2', 'r') as truth:
				for t in truth:
					split = t.split(",")
					if split[-1].strip() == "False":
						label[split[0]] = ["1", "0"]
					elif split[-1].strip()  == "True":
						label[split[0]] = ["1", "1"]
		elif "car >= 3" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/class_count/clip2/car/opt/opt_car_count_2', 'r') as truth:
				for t in truth:
					split = t.split(",")
					if split[-1].strip() == "False":
						label[split[0]] = ["1", "0"]
					elif split[-1].strip()  == "True":
						label[split[0]] = ["1", "1"]
		elif "bus right" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/clip2/opt_bus_right_car', 'r') as truth:
				for t in truth:
					split = t.split(",")
					if split[-1].strip() == "False":
						label[split[0]] = ["1", "0"]
					elif split[-1].strip()  == "True":
						label[split[0]] = ["1", "1"]
		elif "car behind bus" in predicates.lower():
			with open('/home/yannis/Documents/video-query-system-demo/static/results/localisation/clip2/opt_car_behind_bus', 'r') as truth:
				for t in truth:
					split = t.split(",")
					if split[-1].strip() == "False":
						label[split[0]] = ["1", "0"]
					elif split[-1].strip()  == "True":
						label[split[0]] = ["1", "1"]

	prediction = False
	if label[image_list[count]][0] == label[image_list[count]][1]:
		prediction = True

	if len(bbox) == 0:
		return jsonify({"result": {'value':image_list[count], 'prediction': prediction}})
	else:
		return jsonify({"result": {'value':image_list[count], 'prediction': prediction, 'bbox':bbox[image_list[count]]}})
	

@app.route("/index")
@app.route("/", methods=["GET"])
def index():
	return render_template("home.html")


if __name__ == '__main__':
	socketio.run(app, port=5009, debug=True)

import ast

def get_pred_bbox(truth):
	label, bbox = dict(), dict()
	for t in truth:
		split = t.split(",")
		if split[-1].strip() == "False":
			label[split[0]] = ["1", "0"]
		elif split[-1].strip()  == "True":
			label[split[0]] = ["1", "1"]

		json_dict = split[1:-2]
		json_dict = ','.join(json_dict)
		if json_dict == "{}":
			bbox[split[0]] = None
		else:
			json_dict = ast.literal_eval(json_dict)
			for i, d in enumerate(json_dict[split[0]]):
				if i == 0:
					bbox[split[0]] = [d["bbox"]]
				else:
					bbox[split[0]].extend([d["bbox"]])

	return label, bbox

def get_pred_accuracy(truth):
	correct, total = 0., 0.
	for t in truth:
		split = t.split(',')
		if split[-1].strip() == "True":
			correct += 1
		total += 1
	return float(correct)/float(total)
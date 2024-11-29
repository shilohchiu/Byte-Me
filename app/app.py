from flask import Flask, render_template, request, Response, redirect, url_for
import os
# import time
import tensorflow as tf
from PIL import Image
import numpy as np
from datetime import datetime
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
from tensorflow.keras.models import load_model
import os
from matplotlib import pyplot as plt

import classify

app = Flask(__name__)

n = 0 # this serves as an iterator that 
	  # helps name images that are taken
	  # and passed to the learning model

#loading the model
model = load_model(os.path.join('models','melanomamodel.h5'))
model.compile('adam', loss = tf.losses.BinaryCrossentropy(), metrics = ['accuracy'])

#directory to save the images and the logs
os.makedirs('static/images', exist_ok=True)
log_file = 'static/screening_log.txt'

#read the screening log
def read_log():
	if os.path.exists(log_file):
		with open(log_file, 'r') as file:
			return file.readlines()
	return []

#main page where it displays the live feed, result, and log
@app.route('/')
def index():
	result = request.args.get("result", "")
	return render_template('index.html', 
						result=result, 
						log=read_log(),
						message = "Try taking a picture!")

@app.route('/capture', methods=['POST'])
def capture():
	# set the image path to a specific iteration
	global n
	image_path = f"static/images/{n}.jpg"
	n += 1
	# set the text of the button to taking picture... please keep the device still...
	# actually take the image
	os.system("libcamera-still -o " + image_path)

	with open(image_path, 'rb') as preview:
		x = (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + preview.read() + b'\r\n')
	return Response(x, mimetype='multiport/x-mixed-replace; boundary=frame')
	# return "ok"

# The function capture is the function that runs when the 
# capture button is clicked. it is responsible for taking 
# pictures with the camera sensor and returns the most 
# recently taken image ready for display as a binary 
# string.
@app.route('/capture', methods=['POST'])
def capture():
	# set the image path to a specific iteration
	global n
	image_path = f"static/images/{n}.jpg"
	n += 1
	# set the text of the button to taking picture... please keep the device still...

	# actually take the image
	os.system("libcamera-still -o " + image_path)

	with open(image_path, 'rb') as preview:
		x = (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + preview.read() + b'\r\n')
		
	# image text returns to normal

	return Response(x, mimetype='multiport/x-mixed-replace; boundary=frame')
	# return "ok"

# @app.route('/classify') # used to be process
# def classify_image():
# 	# declare path to the image to classify
# 	image_path = f"static/images/{n}.jpg"
# 	# prepare the image to be passed to the learning model

# 	# pass the image to the learning model

# 	# write to the log
# 	with open(log_file, 'a') as log:
# 		log.write(f"{datetime.now()}: {result}, {image_path}\n")

# 	# return the result
# 	return render_template('result.html', result=result)

# executable function
if __name__ == '__main__':
	
	app.run(host='0.0.0.0', port=5000, debug=True)

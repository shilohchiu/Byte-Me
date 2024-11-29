from flask import Flask, render_template, request, Response, redirect, url_for
import os
import time
#from picamera import PiCamera # this doesn't work
import tensorflow as tf
from PIL import Image
import numpy as np
from datetime import datetime

import cv2
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import numpy as np
from matplotlib import pyplot as plt

app = Flask(__name__)

# #camera setup
# camera = picamera.PiCamera()
# camera.resolution = (640, 480)


#loading the model
model = load_model(os.path.join('models','melanomamodel.h5'))
model.compile('adam', loss = tf.losses.BinaryCrossentropy(), metrics = ['accuracy'])

#directory to save the images and the logs
os.makedirs('static/images', exist_ok=True)
log_file = 'static/screening_log.txt'

#stream camera footage on the web page
def gen_frames():
	# while True:
	for _ in range(1000):
		#capture frame by frame

		os.system("libcamera-still -o static/images/live.jpg")
		# time.sleep(0.083)
		with open('static/images/live.jpg', 'rb') as live_img:
			yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + live_img.read() + b'\r\n')

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
	return render_template('index.html', result=result, log=read_log())

@app.route('/capture', methods=['POST'])
def capture_image():
	image_path = 'static/images/pic.jpg'
	#capture image with camera
	os.system("libcamera-still -o " + image_path)
	# camera.start_preview()
	# time.sleep(2) # allow time for the camera to adjust
	# camera.capture(image_path)
	# camera.stop_preview()

	return redirect(url_for('process_image'))

@app.route('/process')
def process_image():
	#load and preprocess the image
	image_path = 'static/images/pic.jpg'
	img = Image.open(image_path)
	img = img.resize((224, 224)) # adjust according to model's requirements
	img_array = np.array(img) / 255.0 #normalizing it
	img_array = np.expand_dims(img_array, axis=0) #add the batch dimension\

	prediction = model.predict(img_array)
	result = "malignant" if prediction[0] > 0.5 else "benign"

	with open(log_file, 'a') as log:
		log.write(f"{datetime.now()}: {result}, {image_path}\n")

	return render_template('result.html', result=result)

@app.route('/video_feed')
def video_feed():
	return Response(gen_frames(),
				    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)

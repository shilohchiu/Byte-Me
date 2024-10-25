import tensorflow as tf
import os
import cv2
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
import cv2
from tensorflow.keras.models import load_model

new_model = load_model(os.path.join('models','melanomamodel.h5'))
new_model.compile('adam', loss = tf.losses.BinaryCrossentropy(), metrics = ['accuracy'])

img = cv2.imread('benigntest3.jpg')
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()

resize = tf.image.resize(img, (256,256))
np.expand_dims(resize, 0)
yhat = model.predict(np.expand_dims(resize/255,0))

yhat_new = new_model.predict(np.expand_dims(resize/255, 0))
if yhat > 0.75:
    print('Predicted class is malignant.')
elif yhat < 0.50:
    print('Predicted class is benign.')
else:
    print('Predicted class is undetermined.')
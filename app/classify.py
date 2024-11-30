
# import needed dependencies
import cv2
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import numpy as np
from matplotlib import pyplot as plt

# load in model is a function that takes no arguments and returns 
# the rendered image classification model.
def load_model(): 
    return tf.keras.models.load_model(os.path.join('models','melanomamodel.h5'))


# load_image is a function that takes a string input 
# that represents the image path of a target file and 
# prepares it for use by the learning model. 
# load_image returns the image in a format that can 
# be used by the learning model.
def load_image(path):
    img = cv2.imread(path)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # plt.show()

    resize = tf.image.resize(img, (256,256))
    np.expand_dims(resize, 0)

    return resize

# predict is a function that takes two arguments, the 
# model and the image that has been loaded and processed.
# predict returns a string that indicates the results of 
# the model.
def predict(model, resize):
    message = "An error has occurred!"
    yhat = model.predict(np.expand_dims(resize/255, 0))
    if yhat > 0.75:
        message = "Predicted class is malignant."
    elif yhat < 0.50:
        message = "Predicted class is benign."
    else:
        message = "Predicted class is indeterminate."
    return message
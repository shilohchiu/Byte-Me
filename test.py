""" this file is used to make sure that the model can be called from the Jupyter Notebook in a regular python file. """

# import needed dependencies
import cv2
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import numpy as np
from matplotlib import pyplot as plt


# load in model
new_model = load_model(os.path.join('models','melanomamodel.h5'))

# load in the image
img = cv2.imread('data/test/benigntest3.jpg')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()

resize = tf.image.resize(img, (256,256))
np.expand_dims(resize, 0)

# using the new model
yhat_new = new_model.predict(np.expand_dims(resize/255, 0))
if yhat_new > 0.75:
    print('Predicted class is malignant.')
elif yhat_new < 0.50:
    print('Predicted class is benign.')
else:
    print('Predicted class is undetermined.')
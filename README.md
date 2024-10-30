# Table of Contents

- [Table of Contents](#table-of-contents)
- [Project Overview](#project-overview)
  - [Goal](#goal)
  - [Hardware](#hardware)
  - [Software](#software)
- [Ideas](#ideas)
- [Documentation](#documentation)
  - [Terminal commands](#terminal-commands)
- [Sources](#sources)

# Project Overview
   ## Goal
    We designed a prototype of a melanoma detection device using Raspberry Pi 4 and a CNN model built in Tensorflow. Our prototype was designed with the intention of making an inexpensive and easy-to-use product.
   ## Hardware
    - Screen (doesn't need to be a touch screen.)
    - Camera 

    3D printed case.

   ## Software

    Deep learning with TensorFlow to classify moles as malignant or benign.

   We use **Flask** to create an app that stores previous screenings and display results of screenings as well as live footage recorded by our camera.


# Ideas
- Flask App to display results
- Transfer image to SQL db ?
- 
# Documentation

## Terminal commands
`source env/bin/activate`
activate the virtual environment w/ needed dependencies in the directory titled final
- Set up the web-app:
`export FLASK_APP=app.py`
`flask run --host=0.0.0.0`
# Sources
| Description | Source |
|-----|-----|
|Information about how convolution neural networks work.|https://keras.io/api/layers/convolution_layers/convolution2d/|
Connecting Jupyter Notebook on Raspberry Pi:
https://www.instructables.com/Jupyter-Notebook-on-Raspberry-Pi/
- Installing TensorFlow 2 on Raspberry Pi:
I used a combination of these sources to debug issues I was having with installing Tensorflow on my Raspberry Pi.
Finally installed it with a pip install tensorflow in my virtual environment after installing needed dependencies.
- https://www.youtube.com/watch?v=FkMWfd9KygA&ab_channel=Engineering_life
- https://www.youtube.com/watch?v=QLZWQlg-Pk0&ab_channel=SamWestbyTech
- https://qengineering.eu/install-tensorflow-on-raspberry-64-os.html
- Useful Image Classification with TensorFlow Tutorial: 
https://www.youtube.com/watch?v=jztwpsIzEGc&ab_channel=NicholasRenotte I used this tutorial to figure out how to build an image classification system.
- Dataset:
https://www.kaggle.com/datasets/fanconic/skin-cancer-malignant-vs-benign
- Connecting TensorFlow to RPi: https://www.reddit.com/r/raspberry_pi/comments/lms6mq/deploying_deep_learning_models_on_raspberry_pi_4_b/
- Visual Studio and Git tutorials
https://superuser.com/questions/1423443/using-visual-studio-and-git-how-do-i-commit-a-new-folder-to-my-git-repository
- Replace depracated module
https://peps.python.org/pep-0594/#imghdr
https://docs.ultralytics.com/guides/model-training-tips/#early-stopping
https://machinelearningmastery.com/how-to-stop-training-deep-neural-networks-at-the-right-time-using-early-stopping/

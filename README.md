# Table of Contents

- [Table of Contents](#table-of-contents)
- [Project Overview](#project-overview)
  - [Goal](#goal)
  - [Hardware](#hardware)
  - [Software](#software)
- [Ideas](#ideas)
- [Documentation](#documentation)
  - [Directories and Files](#directories-and-files)
  - [Terminal commands](#terminal-commands)
    - [Install Necessary Modules](#install-necessary-modules)
    - [Camera commands](#camera-commands)
    - [Steps for checking if tensorflow is correctly installed on RPi](#steps-for-checking-if-tensorflow-is-correctly-installed-on-rpi)
    - [Setting up the web app](#setting-up-the-web-app)
- [Sources](#sources)
  - [Deep Learning Sources](#deep-learning-sources)
  - [Flask Sources](#flask-sources)
  - [Data Sources](#data-sources)
  - [Other Sources](#other-sources)

# Project Overview
   ## Goal
    We designed a prototype of a melanoma detection device using Raspberry Pi 4 and a CNN model built in Tensorflow. Our prototype was designed with the intention of making an inexpensive and easy-to-use product.
   ## Hardware
    - Screen (doesn't need to be a touch screen.)
    - Camera 
    - 3D printed case.
   ## Software
    Deep learning with TensorFlow to classify moles as malignant or benign.
   We use **Flask** to create an app that stores previous screenings and display results of screenings as well as live footage recorded by our camera.
# Ideas
- Flask App to display results
- Transfer image to SQL db ?
- 
# Documentation
## Directories and Files
- the **final** directory acts as a backup for exactly what is on the RPi. It is updated occasionally in case the RPi is somehow corrupted.
- 
## Terminal commands
### Install Necessary Modules
- **Tensorflow:** `pip install tensorflow`
- **OpenCV:** `pip install opencv-python==4.5.3.56`
- **Matplotlib:** `pip install matplotlib`
### Camera commands
- Take a picture: `libcamera-still -o [/path/to/file].jpg` (make sure that the filename/path does not include brackets)
### Steps for checking if tensorflow is correctly installed on RPi
- activate the virtual environment: `source env/bin/activate`. Make sure that the directory of the virtual environment is correct. (The command I used while writing / testing in VSCode was `conda activate myenv` to activate the environment in anaconda.)
- To install Tensorflow, make sure that the virtual environment is activated. Then, `pip install tensorflow`.
- Enter python using `python3`.
- `import tensorflow as tf` and `print(tf.__version__)`. THe version should be 2.17.0
### Setting up the web app
`export FLASK_APP=app.py`
`flask run --host=0.0.0.0`
# Sources
## Deep Learning Sources
| Description | Source |
|-----|-----|
| About convolution neural networks | https://keras.io/api/layers/convolution_layers/convolution2d/|
| Install Jupyter Notebook onto Raspberry Pi | https://www.instructables.com/Jupyter-Notebook-on-Raspberry-Pi/ |
| Installing TensorFlow 2 on Raspberry Pi | https://www.youtube.com/watch?v=FkMWfd9KygA&ab_channel=Engineering_life https://www.youtube.com/watch?v=QLZWQlg-Pk0&ab_channel=SamWestbyTech https://qengineering.eu/install-tensorflow-on-raspberry-64-os.html |
| Use TensorFlow to RPi | https://www.reddit.com/r/raspberry_pi/comments/lms6mq/deploying_deep_learning_models_on_raspberry_pi_4_b/ |
| Image Classification with TensorFlow Tutorial | https://www.youtube.com/watch?v=jztwpsIzEGc&ab_channel=NicholasRenotte |
| Early stopping in Tensorflow | https://docs.ultralytics.com/guides/model-training-tips/#early-stopping https://machinelearningmastery.com/how-to-stop-training-deep-neural-networks-at-the-right-time-using-early-stopping/ |
## Flask Sources
| Flask image input | https://stackoverflow.com/questions/44926465/upload-image-in-flask |
## Data Sources
| Description | Source |
|-----|-----|
| Image dataset | https://www.kaggle.com/datasets/fanconic/skin-cancer-malignant-vs-benign |
## Other Sources
| Description | Source |
|-----|-----|
| Git in Visual Studio Code | https://superuser.com/questions/1423443/using-visual-studio-and-git-how-do-i-commit-a-new-folder-to-my-git-repository |
| Replace depracated module | https://peps.python.org/pep-0594/#imghdr |
| Installing OpenCV | https://raspberrypi-guide.github.io/programming/install-opencv |

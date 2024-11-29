# Table of Contents
- [Table of Contents](#table-of-contents)
- [Project Overview](#project-overview)
  - [Team](#team)
  - [Goal](#goal)
  - [Hardware](#hardware)
  - [Software](#software)
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
  - [Camera Sources](#camera-sources)
  - [Data Sources](#data-sources)
  - [Other Sources](#other-sources)

# Project Overview
   ## Team
   - **Lead Developer**: Shiloh Chiu
   - **Project Manager**: Sophie Rummler
   - **Hardware Technician**: Emily Sturgill
   ## Goal
    Our aim was to explore how advancements in deep learning can contribute to the biomedical field. To do this, we designed a prototype of a melanoma detection device using the Raspberry Pi 4 and a CNN model built in Tensorflow. Our prototype was designed with the intention of making a product that is both inexpensive and easy-to-use.
   ## Hardware
    - Screen:
    - Camera:
    - 3D printed case
   ## Software
   - Deep learning with **TensorFlow** to classify moles as malignant or benign.
   - **Flask** to create an app that stores previous screenings and display results of screenings as well as live footage recorded by our camera.

# Documentation
## Directories and Files
- the **final** directory acts as a backup for exactly what is on the RPi. It is updated occasionally in case the RPi is somehow corrupted.
## Terminal commands
### Install Necessary Modules
- **Tensorflow:** `pip install tensorflow`
- **OpenCV:** `pip install opencv-python==4.5.3.56`
- **Matplotlib:** `pip install matplotlib`
- **Flask-BasicAuth:** `pip install Flask-BasicAuth`
### Camera commands
- Take a picture: `libcamera-still -o [/path/to/file].jpg` (make sure that the filename/path does not include brackets)
- What you can do with libcamera-vid:`libcamera-vid --help`
- Displays a video preview window for 10 seconds: `libcamera-vid -t 10000`
### Steps for checking if tensorflow is correctly installed on RPi
- activate the virtual environment: `source env/bin/activate`. Make sure that the directory of the virtual environment is correct. (The command I used while writing / testing in VSCode was `conda activate myenv` to activate the environment in anaconda.)
- To install Tensorflow, make sure that the virtual environment is activated. Then, `pip install tensorflow`.
- Enter python using `python3`.
- `import tensorflow as tf` and `print(tf.__version__)`. The version should be 2.17.0
### Setting up the web app
- Set up the virtual environment with `source env/bin/activate`
- First, cd into the app directory (cd app).
- `export FLASK_APP=app.py`
- `flask run --host=0.0.0.0`
- Run `` in the browser.
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
## Camera Sources
| Description | Source |
|-----|-----|
| Troubleshooting | https://forums.raspberrypi.com/viewtopic.php?t=368673 |
| Taking a picture w/ libcamera | https://forums.raspberrypi.com/viewtopic.php?t=344092 |
| Live Feed | https://github.com/shashank-shark/rasp-live-feed-flask |
| libcamera-vid info | https://youtu.be/JR1p1dwpT3I |
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

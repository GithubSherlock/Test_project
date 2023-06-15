# Test_project

Video data collection and projective transformation

## Install

**Python3**

The project is based on [Python3](https://www.python.org/downloads/).

**PyCharm**

The IDE software applied in this project is [PyCharm](https://www.jetbrains.com/pycharm/download/).

**Open-CV**

[OpenCV](https://opencv.org/releases/) (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.

OpenCV needs to be used for image processing of image frames and for transformation of person's coordinates and control points in images.

```shell
pip3 install opencv-python
pip3 install opencv-contrib-python
```

After the shell command `pip install opencv-contrib-python` you can choose the latest version. The version applied in this project is 4.7.0.72, So the command used is `pip install opencv-contrib-python==4.7.0.72`.

**numpy**

[Numpy](https://numpy.org/install/) is the fundamental package for scientific computing in Python.

In this project, `numpy` is used to calculate the geographic location of a person in new coordinates after the projective transformation.

```shell
pip3 install numpy
```

**matplotlib**

 [Matplotlib](https://matplotlib.org/stable/index.html) is a comprehensive library for creating static, animated, and interactive visualizations in Python.

The last Python program in this project requires the use of the library `matplotlib` to display the frame animation of person's trajectory.

```shell
pip3 install matplotlib
```

**LabelImg**

[LabelImg](https://github.com/heartexlabs/labelImg#use-docker) is a free, open source tool for graphically labeling images. It’s written in Python and uses QT for its graphical interface.

Pedestrian trajectories from image frames (image ->numbers) tracked manually via LabelImg.

```shell
pip3 install labelImg
labelImg
labelImg [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

## Usage


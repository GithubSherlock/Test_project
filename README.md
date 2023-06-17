# Test_project

Video data collection and projective transformation

## Install

##### Python3

The project is based on [Python3](https://www.python.org/downloads/).

##### PyCharm

The IDE software applied in this project is [PyCharm](https://www.jetbrains.com/pycharm/download/).

##### Open-CV

[OpenCV](https://opencv.org/releases/) needs to be used for image processing of image frames and for transformation of pedestrian's coordinates and control points in images.

```shell
pip3 install opencv-python
pip3 install opencv-contrib-python
```

After the shell command `pip install opencv-contrib-python` you can choose the latest version. The version applied in this project is 4.7.0.72, So the command used is `pip install opencv-contrib-python==4.7.0.72`.

##### numpy

In this project, [numpy](https://numpy.org/install/) is used to calculate the geographic location of a pedestrian in new coordinates after the projective transformation.

```shell
pip3 install numpy
```

##### matplotlib

The last Python program in this project requires the use of the library [matplotlib](https://matplotlib.org/stable/index.html) to display the frame animation of the pedestrian's trajectory, finally save an animation file as a gif in `./output/`.

```shell
pip3 install matplotlib
```

##### xml.etree.ElementTree

The [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module implements a simple and efficient API for parsing and creating XML data.

##### LabelImg

Pedestrian trajectories tracked from image frames manually via [LabelImg](https://github.com/heartexlabs/labelImg#use-docker).

```shell
pip3 install labelImg
labelImg
labelImg [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

## Usage

##### Steps

1. Store a trajectory video file in the folder `input`, then run the file `build_frame_images.py` to get the data about frame number and fps and to get image frames in folder path `./output/output_frames`.
2. Use **LabelImg** to track pedestrian trajectories from image frames (image ->numbers) and save data as XML files in folder path `./annotation`.
3. Run the file `visualizing_pedestrian_trajectory.py` to visualize pedestrian trajectory. Relevant image frames and the gif animation file are saved in the folder path `./output`.

##### Comments

* [Link of original video file](https://seafile.cloud.uni-hannover.de/f/6976b0dd3f9d4e5aae58/)
* [Link of XML files about annotation via LabelImg](https://seafile.cloud.uni-hannover.de/f/2f7359669ec54642858f/)
* Video time = number of frames / fps, number of images = number of frames / frame interval.

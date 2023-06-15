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

The last Python program in this project requires the use of the library  [matplotlib](https://matplotlib.org/stable/index.html) to display the frame animation of pedestrian 's trajectory.

```shell
pip3 install matplotlib
```

##### LabelImg

Pedestrian trajectories tracked from image frames manually via [LabelImg](https://github.com/heartexlabs/labelImg#use-docker).

```shell
pip3 install labelImg
labelImg
labelImg [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

## Usage

##### Steps

1. Store a trajectory video files in the folder `input`, then run the file `GetFrame&FPS.py` to get the data about frame number and fps.
2. Run the file `Video2ImageByFrame.py` to get image frames in folder path `output`.
3. Use LabelImg to tracking pedestrian trajectories from image frames (image ->numbers) and save data as XML files in folder path `annotation`.
4. Run the file `GenerateIC.py` to generate the data about image coordinates of pedestrian then saved as txt file and XML file in folder path `person_IC`.
5. Run the file `projective_transformation.py` to compute the projection transformation matrix and geographic coordinates of pedestrian by control points (relevant information saved in folder `Info_control_points`). The data about geographic coordinates of pedestrian saved as txt file and XML file in folder path `person_GC`.
6. Run the file `visualizing_pedestrian_trajectory.py` to visualizing pedestrian trajectory. Relevant image frames saved in folder path `output_animation` and `output_animation_with_line`.

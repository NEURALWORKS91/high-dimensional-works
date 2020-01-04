import numpy as np
import math
import io
import sys
from simple_waymo_open_dataset_reader import WaymoDataFileReader
from simple_waymo_open_dataset_reader import dataset_pb2, label_pb2
from simple_waymo_open_dataset_reader import utils
import cv2
import matplotlib.pyplot as plt


# file for the tfrecord data
data_file_path = '/home/sambit/WAYMO/segment-1208303279778032257_1360_000_1380_000_with_camera_labels.tfrecord'

if __name__ == "__main__":
    print("============= generating training labels ===============")
    print(np.__version__)

    # read in the tfrecord data file
    datafile = WaymoDataFileReader(data_file_path)
    print(datafile)

    for frame in datafile:
        # we are only interested in the top laser and front camera
        # get top lidar info
        laser_name = dataset_pb2.LaserName.TOP  # lidar name for top lidar from the dataset
        laser = utils.get(frame.lasers, laser_name)
        laser_calibration = utils.get(frame.context.laser_calibrations, laser_name)


        print(laser_calibration)

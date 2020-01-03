import os
import torch
import numpy as np
import matplotlib.pyplot as plt
import cv2
import waymo_open_dataset.dataset_pb2
import waymo_open_dataset.label_pb2
import waymo_open_dataset.utils

if __name__ == '__main__':

    print(torch.__version__)
    print(torch.cuda.is_available())

    mat1 = np.array([1, 2, 3, 4])

    print(mat1)
    pass




# From Python
# It requires OpenCV installed for Python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import cv2
import os
import numpy as np
import scipy.io as sio
from sys import platform

# Remember to add your installation path here
# Option a
dir_path = os.path.dirname(os.path.realpath(__file__))
if platform == "win32": sys.path.append(dir_path + '/../../python/openpose/');
else: sys.path.append('../../python');
# Option b
# If you run `make install` (default path is `/usr/local/python` for Ubuntu), you can also access the OpenPose/python module from there. This will install OpenPose and the python library at your desired installation path. Ensure that this is in your python path in order to use it.
# sys.path.append('/usr/local/python')

# Parameters for OpenPose. Take a look at C++ OpenPose example for meaning of components. Ensure all below are filled
try:
    from openpose import openpose as op
except:
    raise Exception('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
params = dict()
params["logging_level"] = 3
params["output_resolution"] = "-1x-1"
params["net_resolution"] = "-1x368"
params["model_pose"] = "BODY_25"
params["alpha_pose"] = 0.6
params["scale_gap"] = 0.3
params["scale_number"] = 1
params["render_threshold"] = 0.05
# If GPU version is built, and multiple GPUs are available, set the ID here
params["num_gpu_start"] = 0
params["disable_blending"] = False
# Ensure you point to the correct path where models are located
params["default_model_folder"] = dir_path + "/../../../models/"
# Construct OpenPose object allocates GPU memory
openpose = op.OpenPose(params)

while 1:
    # Read new image
    #img = cv2.imread("../../../examples/media/right.jpg")
    img = cv2.imread("right.jpg")
    #img = cv2.imread("../../../examples/media/COCO_val2014_000000000192.jpg")
    # Output keypoints and the image with the human skeleton blended on it
    keypoints, output_image = openpose.forward(img, True)
    # Print the human pose keypoints, i.e., a [#people x #keypoints x 3]-dimensional numpy object with the keypoints of all the people on that image
    # print(keypoints)
    # print('the shape of output keypoints is ', np.shape(keypoints))
    # print('the type of keypoints is ', type(keypoints))
    # np.savetxt('keypointsfile', keypoints)
    # sio.savemat('./keypoints_test',mdict={'out': keypoints}, oned_as='row')
    # matdata = sio.loadmat('./keypoints_test')
    # print(matdata)
    # Display the image
    np.save( 'right',keypoints)
    cv2.imshow("output", output_image)
    cv2.waitKey(1)

    # break

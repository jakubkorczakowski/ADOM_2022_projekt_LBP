# import the necessary packages
from pyimagesearch.localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import pathlib
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True,
	help="path to the training images")
ap.add_argument("-e", "--testing", required=True, 
	help="path to the tesitng images")
args = vars(ap.parse_args())

# initialize the local binary patterns descriptor along with
# the data and label lists

# loop over the training images
for imagePath in pathlib.Path(args["training"]).rglob('*'):
    # load the image, convert it to grayscale, and describe it
    image = cv2.imread(str(imagePath))

    scale_percent = 20 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    pathlib.Path(imagePath.parent / imagePath.stem.split("_")[0]).mkdir(exist_ok=True)
    succes = cv2.imwrite(str(pathlib.Path(imagePath.parent / imagePath.stem.split("_")[0] / imagePath.name)), resized)
    print(succes)
    print(str(pathlib.Path(imagePath.parent / imagePath.stem.split("_")[0] / imagePath.name)))
    # extract the label from the image path, then update the
    # label and data lists
    # print(pathlib.Path(imagePath.parent / imagePath.stem.split("_")[0] / imagePath.name))

# loop over the testing images
# for imagePath in pathlib.Path(args["testing"]).rglob('*'):
#     # load the image, convert it to grayscale, describe it,
#     # and classify it
#     image = cv2.imread(str(imagePath))

#     scale_percent = 20 # percent of original size
#     width = int(image.shape[1] * scale_percent / 100)
#     height = int(image.shape[0] * scale_percent / 100)
#     dim = (width, height)

#     # resize image
#     resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

#     succes = cv2.imwrite(str(imagePath), resized)
#     print(succes)


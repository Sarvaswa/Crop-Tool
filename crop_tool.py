# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 18:17:18 2017

@author: Sarvaswa
"""

## Script to capture Click event and crop an image

from __future__ import print_function
from win32api import GetSystemMetrics
import argparse
import cv2
import os

## Initialize the list of reference points and boolean indicating
## whether cropping is being performed or not
refPt = []
is_cropping = False

def click_and_crop(event, x, y, flags, param):
    
    # grab references to the global variables
    global refPt, is_cropping
    
    # If left mouse button was pressed, record starting points of the crop
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x,y)]
        is_cropping = True
    
    # If left mouse button was released, record end points of the crop and
    # create a rectangle around the ROI
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x,y))
        is_cropping = False
        
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow('Image', image)

## Construct the argument parser object and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help='Path to the Image')
args = vars(ap.parse_args())

## Load the image, clone it, and setup the mouse callback function
print('Starting Crop Tool ...')
image = cv2.imread(args['image'])
clone = image.copy()

## Resize image if bigger than screen resolution
screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)
img_height, img_width = image[:,:,0].shape
factor = 1
if (img_width > screen_width) or (img_height > screen_height):
    widthDiff  = img_width - screen_width
    heightDiff = img_height - screen_height
    if widthDiff > heightDiff:
        print('Original image is wider than the screen, resizing ...')
        factor = screen_width/img_width
        image  = cv2.resize(image, (int(img_width*factor), int(img_height*factor)),
                            interpolation = cv2.INTER_LANCZOS4)
    else:
        print('Original image is taller than the screen, resizing ...')
        factor = screen_height/img_height
        image  = cv2.resize(image, (int(img_width*factor), int(img_height*factor)),
                            interpolation = cv2.INTER_LANCZOS4)

clone_resized = image.copy()

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', click_and_crop)

# Keep looping until 'c' is pressed
while True:
    cv2.imshow('Image', image)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('r'):
        image = clone_resized.copy()
    elif key == ord('c'):
        if len(refPt) == 2:
            refPt = [(int(pt[0]/factor), int(pt[1]/factor)) for pt in refPt]
            roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
            cv2.imshow('ROI', roi)
            key1 = cv2.waitKey(0)
            cv2.destroyWindow('ROI')
            if key1 == ord('s'):
                crops_path = 'crops/'
                numFiles = len([fname for fname in os.listdir(crops_path) if fname.endswith('.png')])
                new_filename = str(numFiles + 1) + '.png'
                cv2.imwrite(crops_path + new_filename, roi)
                print('Cropped Image saved to: ', crops_path + new_filename)
        else:
            print('Draw a rectangle across the cropping region first.')
    elif key == 27:
        break

cv2.destroyAllWindows()
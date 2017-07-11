# Crop_Tool
A Command line tool for cropping images, written in Python.  
Inspired by Adrian Rosebrock's " Capturing mouse click events with Python and OpenCV " tutorial at the following link:  
http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/

# Added Features
* Save Crops to file
* Make multiple crops in a single session
* Crop independent of the crop direction
* Backward compatibility (Written in Python 3.5, works in Python 2.7)
* Auto resizing the image to fit the screen

# Requirements
* Pyhton (Tested on 2.7 and 3.5)
* OpenCV
* Win32API (Install using ```pip install pypiwin32```)

# Usage
Create a directory named 'Crops' inside the root directory of the project  
Open Command Line and type the following command  
``` python crop_tool.py --image PATH_TO_IMAGE```  
```PATH_TO_IMAGE``` is the path of the image file you want to crop 

This opens a window displaying the image  
Click on the starting point of the crop, drag the mouse till the end point and release it  
A green rectangle would appear  

Press 'c' to preview the crop  
Press 's' to save the crop to the 'Crops' directory  
Press 'r' to reset the image (removes the green rectangle from the original image)  
Press 'Esc' to end the cropping session  

**NOTE:** Saving can only work after pressing 'c' i.e. after previewing the crop

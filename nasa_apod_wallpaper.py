'''
Created on Sep 22, 2019

@author: Austin Owens

NASA's Astronomy Picture of the Day (APOD) for wallpaper
'''

import os
import ctypes
from six.moves import urllib

URL = "https://apod.nasa.gov/apod/"

# Fill out where you want to place the APOD pictures. Make sure the directory exists.
OUTPUT_FOLDER = "<SPECIFY_DISIRED_OUTPUT_DIR_TO_PLACE_PICTURES>"

html_file = urllib.request.urlopen(URL)
for line in html_file:
    line = line.decode()
    if "image/" in line and ".jpg" in line:
        print(line)
        pic_path = line.split('<a href="')[1].split('"')[0]
        break

#Checks to see if the image is already there
if not os.path.exists(OUTPUT_FOLDER+pic_path):
    
    #Checks to see if the directories that are needed for the picture are all there
    if not os.path.exists(os.path.dirname(OUTPUT_FOLDER+pic_path)):
        os.makedirs(os.path.dirname(OUTPUT_FOLDER+pic_path))

    print(repr(URL+pic_path))
    pic = urllib.request.urlopen(URL+pic_path)
    with open(OUTPUT_FOLDER+pic_path, "wb") as f:
        f.write(pic.read())
        
else:
    print ("Image already retrieved.")

SPI_SETDESKWALLPAPER = 20 
SPIF_UPDATEINIFILE = 1
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(OUTPUT_FOLDER+pic_path), SPIF_UPDATEINIFILE)

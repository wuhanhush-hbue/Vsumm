#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:38:12 2019

@author: swati
#"""
import sys
import argparse

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    print( "PATH..", pathIn)
    print( "PATH OUT..", pathOut)

    vidcap = cv2.VideoCapture(pathIn)
    print(vidcap)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      fps = vidcap.get(cv2.cv.CV_CAP_PROP_FPS)
      print(fps)
      n_frames = int(vidcap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
      print('nframes', n_frames)

      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      print("COUNT", count)
      cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
      count += 1

if __name__=="__main__":
    print("aba")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)
    
    
#import cv2
#vidcap = cv2.VideoCapture('/home/swati/Documents/pytorch-vsumm-reinforce-master/SumMe/videos/Video_2.mp4')
#success,image = vidcap.read()
#count = 0
#success = True
#while success:
#  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)) 
#  success,image = vidcap.read()
#  print('Read a new frame: ', success)
#  cv2.imwrite('/home/swati/Documents/pytorch-vsumm-reinforce-master/'+ "\\frame%d.jpg" % count, image)     # save frame as JPEG file
#  count += 1
#  vidcap.release()
#
#














































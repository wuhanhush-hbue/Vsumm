#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:21:51 2019

@author: swati
"""

import torch
#print(dir(models))
from torchvision import transforms
#from tqdm import tqdm
import cv2
import time
import os, sys
sys.path.append('../')
import h5py
import sys



#resnet = models.resnet152(pretrained = True)
#print(resnet)
class Generate_dataset:
    def __init__(self, video_path, save_path):
        self.video_path = ""
        self.video_list = []
        self.dataset = {}
        self.frame_root_path = "/home/swati/Documents/pytorch-vsumm- generate dataset-master/frames"
        self.h5_file =  h5py.File(save_path, 'w')
        self._set_video_list(video_path)
        
    def _set_video_list(self, video_path):
#            os.path.isdir(video_path)
            self.video_path = video_path
            print("Vidpath", video_path)
#            self.video_list = os.listdir(video_path)
#            print("vp",video_path)
#            self.video_list.sort()
#            for idx, file_name in enumerate(self.video_list):
#                self.dataset['video_{}'.format(idx+1)] = {}
#                self.h5_file.create_group('video_{}'.format(idx+1))
    def video_to_frames(self):
#         for video_idx, video_filename in enumerate(self.video_list):
#            video_path = video_filename
#            
#            os.path.isdir(video_path)
            
#            video_path = os.path.join(video_path, video_filename)
#            print("path is", video_path)
#            video_basename = os.path.basename(video_path).split('.')[0]
#            print("video_basename is", video_basename)
##            for i in video_path:
##                print()
#            print(video_path)
            count = 1

            video_capture = cv2.VideoCapture(self.video_path)
            print(video_capture)
            success, frame = video_capture.read()
            success = True
            #print("fr", frame)
            while success:
                video_capture.set(cv2.CAP_PROP_POS_MSEC,(count*100))
                
                success, frame = video_capture.read()
                print ('Read a new frame: ', success)
#                print('fps is', fps)
                #Resize = cv2.resize(frame, (224, 224))

                n_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
                print('nframes', n_frames)
#            else:
#                print("break")
               
#            frame_idx % 15 == 0
#            for frame_idx in tqdm(range(n_frames-1)):
               
            
            #img_filename = "{}.jpg".format(str(count).zfill(5))
                #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #frame = cv2.resize(frame, (224, 224))
                #print("frame is ", frame)
                cv2.imwrite("/home/swati/Documents/pytorch-vsumm- generate dataset-master/frames" + ".png", frame)
                count = count + 1
                video_capture.release()

if __name__ == "__main__":
    
    gen = Generate_dataset('/home/swati/Documents/pytorch-vsumm- generate dataset-master/videos/Video_1.mp4', 'new12.h5')
    #gen._set_video_list('/home/swati/Documents/pytorch-vsumm- generate dataset-master/videos/')
    gen.video_to_frames()
#    gen.h5_file.close()
#    









#"converting videos into frames"
#def extractImages(pathIn, pathOut, sec):
#    sec = 0
#    count = 1
#    frameRate = 0.15
#    vidcap = cv2.VideoCapture(pathIn)
#    success,image = vidcap.read()
#    success = extractImages(sec)
#    while success:
#      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
#      success,image = vidcap.read()  
#      print ('Read a new frame: ', success)
#      cv2.imwrite( pathOut + str(count)+ ".png", image)     # save frame as JPEG file
#      count = count + 1
#      sec = sec + frameRate
#      sec = round(sec, 2)
#      return extractImages(sec)
##
#if __name__=="__main__":
#    print("aba")
#    a = argparse.ArgumentParser()
#    a.add_argument("--pathIn", help="path to video")
#    a.add_argument("--pathOut", help="path to images")
#    args = a.parse_args()
#    print(args)
#    extractImages(args.pathIn, args.pathOut, 0)
    
#import cv2
#vidcap = cv2.VideoCapture('video.mp4')
#def getFrame(sec):
#    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
#    hasFrames,image = vidcap.read()
#    if hasFrames:
#        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
#    return hasFrames
#sec = 0
#frameRate = 0.5 #//it will capture image in each 0.5 second
#count=1
#success = getFrame(sec)
#while success:
#    count = count + 1
#    sec = sec + frameRate
#    sec = round(sec, 2)
#    success = getFrame(sec)
#        
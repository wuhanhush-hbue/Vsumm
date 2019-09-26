#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:53:15 2019

@author: swati
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:21:51 2019

@author: swati
"""
#
#import torch
##print(dir(models))
#from torchvision import transforms
#from tqdm import tqdm
import os, sys
sys.path.append('../')
from CNN import ResNet
#from cpd_auto import cpd_auto
from tqdm import tqdm
import math
import cv2
import numpy as np
import h5py
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



#resnet = models.resnet152(pretrained = True)
#print(resnet)
class Generate_dataset:
    def __init__(self, video_path, save_path):
        self.resnet = ResNet()
        self.video_path = ""
        self.video_path1= "/home/swati/Documents/pytorch-vsumm- generate dataset-master/frames/"
        self.video_list = []
        self.dataset = {}
        self.frame_root_path = "/home/swati/Documents/pytorch-vsumm- generate dataset-master/frames1"
        self.h5_file =  h5py.File(save_path, 'w')
        self._set_video_list(video_path)
#        self.count = 1
        self.video_list1 = []
        
    def _set_video_list(self, video_path):
            os.path.isdir(video_path)
            self.video_path = video_path
            video_path1 = video_path
            print("Vidpath", video_path)
            self.video_list = os.listdir(video_path)
            self.video_list1 = os.listdir(video_path1)           
            print("vp",video_path)
            self.video_list.sort()
            for idx, file_name in enumerate(self.video_list):
                self.dataset['video_{}'.format(idx+1)] = {}
                self.h5_file.create_group('video_{}'.format(idx+1))
                
    def _extract_feature(self):
        for frame_idx, frame_filename in enumerate((self.video_list1)):
            video_path1 = self.video_path1
            
            os.path.isdir(video_path1)
            
            video_path1 = os.path.join(video_path1, frame_filename)
            
            frame = cv2.cvtColor(frame_idx, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame_idx,(224, 224))
            print("frame is ", frame)
            res_pool5 = self.resnet(frame_idx)
            frame_feat = res_pool5.cpu().data.numpy().flatten()
            print(frame_feat)

#        return frame_feat
                
  
    def video_to_frames(self):
         for video_idx, video_filename in enumerate(self.video_list):
           
            video_path = self.video_path
            
            os.path.isdir(video_path)
            
            video_path = os.path.join(video_path, video_filename)
            
            video_basename = os.path.basename(video_path).split('.')[0]
            print("video_basename is", video_basename)
            print("printpath", video_path)
            video_capture = cv2.VideoCapture(video_path)
#            print(video_capture)
#            success, frame = video_capture.read()
            count = 1
            success = True
            #print("fr", frame)
            while success:
                
                fps = video_capture.get(cv2.cv.CV_CAP_PROP_FPS)
                print(fps)
                n_frames = int(video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
                print('nframes', n_frames)
                
                success,frame = video_capture.read()
                print("FRAME", frame)     
                print ('Read a new frame: ', success)
                print("COUNT", count)
                print("ROOTPATH", self.frame_root_path)
                print("BASENAME", video_basename)
                
                img_filename = "/frame%d.jpg" % count
                print("PATH",("/home/swati/Documents/pytorch-vsumm- generate dataset-master/frames1/"+ video_basename + img_filename))
                cv2.imwrite(os.path.join("/home/swati/Documents/pytorch-vsumm- generate dataset-master/frames1/" + video_basename + img_filename), frame)
#                
                count += 1       
                
#                video_capture.release()
                
   


if __name__ == "__main__":
    
    gen = Generate_dataset('/home/swati/Documents/pytorch-vsumm- generate dataset-master/videos/', 'new22.h5')
    #gen._set_video_list('/home/swati/Documents/pytorch-vsumm- generate dataset-master/videos/')
    gen._extract_feature()
    gen.h5_file.close()
#import cv2     
#import os
#cap = cv2.VideoCapture('/home/swati/Documents/pytorch-vsumm- generate dataset-master/videos/Video_1.mp4')
#print("CAp is", cap)
#cap.isOpened()
#success,image = cap.read()
#count = 1
#success = True
#while success:
#     cv2.imwrite("image%d.jpg" % count, image)     # save frame as JPEG file
#     success,image = cap.read()
#     print("Read new frame", success)
#     
#     count += 1
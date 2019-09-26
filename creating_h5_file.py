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
from cpd_auto import cpd_auto
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
        self.video_path = ""
        self.video_list = []
        self.dataset = {}
        self.frame_root_path = "/home/swati/Documents/pytorch-vsumm- generate dataset-master/frames1"
        self.h5_file =  h5py.File(save_path, 'w')
        self._set_video_list(video_path)
        
    def _set_video_list(self, video_path):
            os.path.isdir(video_path)
            self.video_path = video_path
            print("Vidpath", video_path)
            self.video_list = os.listdir(video_path)
            print("vp",video_path)
            self.video_list.sort()
            for idx, file_name in enumerate(self.video_list):
                self.dataset['video_{}'.format(idx+1)] = {}
                self.h5_file.create_group('video_{}'.format(idx+1))
                
    def _extract_feature(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (224, 224))
        print("frame is ", frame)
        res_pool5 = self.resnet(frame)
        frame_feat = res_pool5.cpu().data.numpy().flatten()

        return frame_feat
    
    def _save_dataset(self):
        pass

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
            success, frame = video_capture.read()
            count = 1
            success = True
            #print("fr", frame)
            while success:
                
                fps = video_capture.get(cv2.CV_CAP_PROP_FPS)
                print(fps)
                n_frames = int(video_capture.get(cv2.CV_CAP_PROP_FRAME_COUNT))
                print('nframes', n_frames)
                
                success,frame = video_capture.read()
                
                picks = []
                video_feat = None
                video_feat_for_train = None
                for frame_idx in tqdm(range(n_frames-1)):
                    success, frame = video_capture.read()
                if success:
                    frame_feat = self._extract_feature(frame)
                    print(frame)

                    if frame_idx % 15 == 0:
                        picks.append(frame_idx)

                        if video_feat_for_train is None:
                            video_feat_for_train = frame_feat
                        else:
                            video_feat_for_train = np.vstack((video_feat_for_train, frame_feat))

                    if video_feat is None:
                        video_feat = frame_feat
                    else:
                        video_feat = np.vstack((video_feat, frame_feat))

                    img_filename = "{}.jpg".format(str(frame_idx).zfill(5))
                    print("frame is ", frame)

                    cv2.imwrite(os.path.join(self.frame_root_path, video_basename, img_filename), frame)

                else:
                    print("frame is..")
                    break

               
                print ('Read a new frame: ', success)
                print("COUNT", count)
                print("ROOTPATH", self.frame_root_path)
                print("BASENAME", video_basename)
#                print("COUNT", self.count)
                
#            for filename in enumerate("/home/swati/Documents/pytorch-vsumm- generate dataset-master/frames/"):
                img_filename = "/frame%d.jpg" % count
                print("PATH",("/home/swati/Documents/pytorch-vsumm- generate dataset-master/frames1/"+ video_basename + img_filename))
                cv2.imwrite(os.path.join("/home/swati/Documents/pytorch-vsumm- generate dataset-master/frames1/" + video_basename + img_filename), frame)
#                print("FILENAME", img_filename)
##                path_new = 'frames/' + "frame" + str(self.count)+ ".jpg"
##                print(str(path_new))
#                path = os.path.join(self.frame_root_path, video_basename, img_filename)
#                print ("PATH IS", path)
#                cv2.imwrite(self.frame_root_path + 'frames/'+ "\\frame%d.jpg" % count, frame)
        
#                cv2.imwrite( self.frame_root_path +'frames/' + '\\Video_%d'+'\\frame%d.jpg' % self.count, frame)     # save frame as JPEG file
                count += 1
#                video_capture.release()

if __name__ == "__main__":
    
    gen = Generate_dataset('/home/swati/Documents/pytorch-vsumm- generate dataset-master/videos/', 'new22.h5')
    #gen._set_video_list('/home/swati/Documents/pytorch-vsumm- generate dataset-master/videos/')
    gen.video_to_frames()
    gen.h5_file.close()
#    










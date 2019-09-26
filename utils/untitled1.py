#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:23:53 2019

@author: swati
"""

import h5py
         
           
f = h5py.File('/home/swati/Documents/pytorch-vsumm- generate dataset-master/actionfinal.h5','a')
f.create_dataset('Video_1/user_summary', dtype = "i8", shape=(15, 108) )
f.create_dataset('Video_2/user_summary', dtype = "i8", shape=(15, 93) )
f.create_dataset('Video_3/user_summary', dtype = "i8", shape=(15, 201) )
f.create_dataset('Video_4/user_summary', dtype = "i8", shape=(15, 151) )
f.create_dataset('Video_5/user_summary', dtype = "i8", shape=(15, 259) )
f.create_dataset('Video_6/user_summary', dtype = "i8", shape=(15, 172) )
f.create_dataset('Video_7/user_summary', dtype = "i8", shape=(15, 239) )
f.create_dataset('Video_8/user_summary', dtype = "i8", shape=(15, 361) )
f.create_dataset('Video_9/user_summary', dtype = "i8", shape=(15, 205) )
f.create_dataset('Video_10/user_summary', dtype = "i8", shape=(15, 65) )
f.create_dataset('Video_11/user_summary', dtype = "i8", shape=(15, 201) )
f.close()
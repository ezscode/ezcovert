#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   video2imgs.py
@Time    :   2025-01-18 11:49:06
@Author  :   Ez
@Version :   1.0
@Desc    :   None


requirements: 

opencv-python==4.10.0.84

'''



import os 
import sys 
import cv2 
from pathlib import Path

def video2images(video_path, save_dir):
    times = 0
    
    # PAL 制式每秒钟25帧，NTSC制式每秒钟30帧 
    # 提取视频的频率，每1帧提取一个
    frame_frequency = 25  # 25--30 
    
	# 如果文件目录不存在则创建目录
    if not os.path.exists(save_dir):os.makedirs(save_dir)
        
    # 读取视频帧
    camera = cv2.VideoCapture(video_path)
    
    while True: 
        times = times + 1
        res, image = camera.read()
        if not res:
            print('not res , not image')
            break

        # 按照设置间隔存储视频帧
        save_path = os.path.join(save_dir, str(times)+'.jpg')
        if times % frame_frequency == 0:
            cv2.imwrite(save_path, image) 

    print('图片提取结束') 
    # 释放摄像头设备
    camera.release()
 

def handle_paths(paths):
    for path in paths:  
        if os.path.isfile(path):  
            save_dir = Path(path).with_suffix("").as_posix() + '-split'
            if not os.path.isdir(save_dir):os.makedirs(save_dir) 
            video2images(path, save_dir)
    

if __name__ == '__main__':
    
    paths = sys.argv[1:]
    print('-- ', paths)   
    handle_paths(paths) 
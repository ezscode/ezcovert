#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   video2audio.py
@Time    :   2025-01-18 11:42:36
@Author  :   Ez
@Version :   1.0
@Desc    :   None


requirements: 

moviepy==2.0.0
ffmpeg==1.4

'''



import os 
import sys 
import moviepy.editor as mp   


# 从视频中提取音频
def extract_audio(video_path, audio_path=''):
    if len(audio_path) == 0:
        audio_path = video_path + '_eaudio.mp3'
    my_clip = mp.VideoFileClip(video_path)
    my_clip.audio.write_audiofile(audio_path) 



def handle_paths(paths):
    for path in paths:  
        if os.path.isfile(path):
            extract_audio(path)
            
        if os.path.isdir(path):
            save_dir = path + '_audio'
            if not os.path.isdir(save_dir):os.makedirs(save_dir) 
            for file_name in os.listdir(path):
                file_path = os.path.join(path, file_name)
                save_path = os.path.join(save_dir, file_name + '.mp3')  
                if os.path.isfile(file_path):
                    extract_audio(file_path, save_path) 




if __name__ == '__main__':
    
    paths = sys.argv[1:]
    print('-- ', paths)   
    handle_paths(paths) 
    


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   video2audio.py
@Time    :   2025-01-18 11:42:36
@Author  :   Ez
@Version :   1.0
@Desc    :   None


requirements: 

brew install ffmpeg

'''

import os
import subprocess
from tkinter import Tk, filedialog, messagebox

def mov2mp3(file_path, save_path):
    command = [
        'ffmpeg',
        '-i', file_path,
        '-q:a', '0',
        '-map', 'a',
        save_path
    ]
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error processing {file_path}: {e}")
        return False
    



def handle_paths(paths):
    for path in paths:  
        if os.path.isfile(path):
            mov2mp3(path)
            
        if os.path.isdir(path):
            save_dir = path + '_audio'
            if not os.path.isdir(save_dir):os.makedirs(save_dir) 
            for file_name in os.listdir(path):
                file_path = os.path.join(path, file_name)
                save_path = os.path.join(save_dir, file_name + '.mp3')  
                if os.path.isfile(file_path):
                    mov2mp3(file_path, save_path) 




if __name__ == '__main__':
    
    paths = sys.argv[1:]
    print('-- ', paths)   
    handle_paths(paths) 
    


#!/usr/bin/env python3
import os
root_dir=os.getcwd()
name=['Source_code','Animation','Png','Data']
def fmove(files,destin):
    os.system('mv {} {}'.format(files,destin))
for directory in os.listdir():
    if os.path.isdir(directory) and not directory.split('/')[-1]=='.git':
        os.chdir(directory)
        for nam in name:
            if not os.path.exists(nam):
                os.mkdir(nam)
        os.chdir(root_dir)
for directory in os.listdir():
    if os.path.isdir(directory) and not directory.split('/')[-1]=='.git':
        os.chdir(directory)
        for files in os.listdir():
            if os.path.isfile(files):
                if os.path.splitext(files)[-1]=='.py' and not files=='video_merger.py':
                    fmove(files,name[0])
                elif os.path.splitext(files)[-1]=='.mp4' or files=='video_merger.py':
                    fmove(files,name[1])
                elif os.path.splitext(files)[-1]=='.png':
                    fmove(files,name[2])
                else:
                    fmove(files,name[3])
        os.chdir(root_dir)                    

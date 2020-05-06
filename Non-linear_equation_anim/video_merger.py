from moviepy.editor import *
import os
import sys
os.system('ls {}>video_file.txt'.format(sys.argv[1]))
fl=open('video_file.txt','r')
videos=[]
for file_name in fl:
    videos.append(VideoFileClip(file_name[0:-1]))
merged=concatenate_videoclips(videos)
merged.write_videofile('ZFinal_animation.mp4',codec='libx264')


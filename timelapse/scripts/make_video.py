import os
import json
import time
import shutil
from subprocess import Popen
from timelapse.copy_files_for_video import copy_files_for_video
from timelapse.make_video import make_video
from timelapse import utils


with open('camera_settings.json') as f:
    camera_settings = json.load(f)


def main():
    print('start make video', time.asctime())
    
    camera_main_dir = camera_settings['main_dir']
    tmp_dir = os.path.join(utils.STORAGE_DIR, camera_main_dir, utils.TMP)
    
    if os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir)
        
    os.mkdir(tmp_dir)
    
    photos_dir = os.path.join(utils.STORAGE_DIR, camera_main_dir, utils.PHOTOS_BY_TIME_DIR)
    copy_files_for_video(photos_dir, tmp_dir)
    
    video_dir = os.path.join(utils.STORAGE_DIR, camera_main_dir, utils.VIDEOS_DIR)
    make_video(tmp_dir, video_dir)
    
    print('finish make video', time.asctime())
 

if __name__ == '__main__':
    main()

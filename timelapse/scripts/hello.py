import os
# import requests
# import schedule
# import json
# import time
# import shutil
import subprocess
from subprocess import Popen
from timelapse.copy_files_for_video import copy_files_for_video

src_path = 'C:\\timelapse\\storage\\Camera1935\\videos\\v.mp4'
out_path = 'C:\\timelapse\\storage\\Camera1935\\photos'

command = f'ffmpeg -y -r 25 -i {out_path}\\img-%06d.jpg -vcodec libx264 {src_path}'

def main():
    print("Hello!")
    
    # copy_files_for_video(src_path, out_path)
    
    print(1)
    
    # os.system(command)
    subprocess.run(command)
    # p = Popen(command)
    
    print(2)
    
    # print(p.communicate())
    
    # p.terminate()
    
    # def do():
    #     print("Hello!")
    
    #schedule.every(2).seconds.do(do)

    # while True:
    #     # schedule.run_pending()
    #     print(666)
    #     time.sleep(1)

if __name__ == '__main__':
    main()

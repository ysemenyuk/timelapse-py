import os
import time
import subprocess


def make_video(dir_with_photo_path, dir_for_video_path, video_name='video.mp4'):
    # print('sart make video', time.asctime())
    
    video_file_path = os.path.join(dir_for_video_path, video_name)
    command = f'ffmpeg -y -r 25 -i {dir_with_photo_path}\\img-%06d.jpg -vcodec libx264 {video_file_path}'
    subprocess.run(command)
    
    # print('finish make video', time.asctime())
    

if __name__ == '__main__':
    make_video()

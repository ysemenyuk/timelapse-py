import os
import time
import json
from timelapse.save_photo import save_photo
from timelapse import utils


with open('camera_settings.json') as f:
    camera_settings = json.load(f)


def make_dir_path(camera_settings):
    camera_main_dir = camera_settings['main_dir']
    dir_name = time.strftime('%Y-%m-%d')
    dir_path = os.path.join(utils.STORAGE_DIR, camera_main_dir, utils.PHOTOS_BY_TIME_DIR, dir_name)
    return dir_path


def main():
    print(time.asctime())
    interval = camera_settings['save_photo_interval']
    photo_url = camera_settings['photo_url']
    start_time = camera_settings['save_photo_start_time']
    stop_time = camera_settings['save_photo_stop_time']
    
    while True:
        if start_time < time.strftime('%H-%M') < stop_time:
            dir_path = make_dir_path(camera_settings)
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path)
                print("Directory '% s' created" % dir_path)
            save_photo(photo_url, dir_path)
        else:
            print('out of time')
       
        print('wait', interval, 'seconds')
        time.sleep(interval)


if __name__ == '__main__':
    main()

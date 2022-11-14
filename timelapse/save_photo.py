import os
import requests
import time


def make_photo_name():
    st = str(time.strftime('%Y-%m-%d--%H-%M-%S'))
    return f'img--{st}.jpg'

def save_photo(photo_url, dir_path):
    print('start save_photo', time.asctime())
   
    response = requests.get(photo_url)

    if response.status_code == 200:
        print("response code '% s'" % response.status_code)
        photo_name = make_photo_name()
        photo_path = os.path.join(dir_path, photo_name)
        # print('photo_path: ', photo_path)

        with open(photo_path, "wb") as f:
            f.write(response.content)
            print("photo saved successfully '% s'" % photo_path)
    else:
        print("response code '% s'" % response.status_code)


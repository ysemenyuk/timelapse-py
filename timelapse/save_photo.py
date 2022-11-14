import os
import requests
import time


def make_photo_name():
    st = str(time.strftime('%Y-%m-%d--%H-%M-%S'))
    return f'img--{st}.jpg'

def save_photo(photo_url, dir_path):
    print('start save_photo', time.asctime())

    response = {}
   
    try:
        response = requests.get(photo_url)
    except Exception as e:
        print('except requests error', e)

    if response and response.status_code == 200:
        print("response code '% s'" % response.status_code)
        photo_name = make_photo_name()
        photo_path = os.path.join(dir_path, photo_name)
        # print('photo_path: ', photo_path)

        with open(photo_path, "wb") as f:
            f.write(response.content)
            print("photo saved successfully '% s'" % photo_path)
    elif response and response.status_code:
        print("response code '% s'" % response.status_code)
    else:
        print("failed to save photo")


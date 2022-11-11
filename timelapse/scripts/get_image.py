import os
import requests
import time

url = 'https://apod.nasa.gov/apod/image/1701/potw1636aN159_HST_2048.jpg'
parent_dir = ''

def make_dir_name():
    return str(time.strftime('%Y-%m-%d'))

def make_image_name():
    st = str(time.strftime('%Y-%m-%d--%H-%M-%S'))
    return f'img--{st}.jpg'

def main():
    print(time.asctime())

    dir_name = make_dir_name()
    dir_path = os.path.join(parent_dir, dir_name)
    print('dir_path: ', dir_path)

    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
        print("Directory '% s' created" % dir_path)
    
    response = requests.get(url)

    if response.status_code == 200:
        print("response code '% s'" % response.status_code)
        img_name = make_image_name()
        img_path = os.path.join(dir_path, img_name)
        print('img_path: ', img_path)

        with open(img_path, "wb") as f:
            f.write(response.content)
            print("Image '% s' created" % img_path)
    else:
        print("response code '% s'" % response.status_code) 


if __name__ == '__main__':
    main()
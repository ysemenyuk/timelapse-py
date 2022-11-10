import os
import requests

def main():
    print("Hello!")
    url = 'https://apod.nasa.gov/apod/image/1701/potw1636aN159_HST_2048.jpg'
    response = requests.get(url)

    # f_ext = os.path.splitext(url)[-1]
    # f_name = 'img{}'.format(f_ext)

    f_name = url.split("/")[-1]

    if response.status_code == 200:
        with open(f_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code) 

if __name__ == '__main__':
    main()
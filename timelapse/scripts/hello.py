import os
# import requests
# import json
# import time
# import schedule
# import shutil
# import subprocess
# from subprocess import Popen
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Hello!")
    print(os.environ.get('STORAGE_DIR'))
    print(os.getenv('STORAGE_DIR'))

    # for item, value in os.environ.items():
    #     print('{}: {}'.format(item, value))
    # def do():
    #     print("Hello!")
    
    # schedule.every(2).seconds.do(do)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

if __name__ == '__main__':
    main()

import threading
import os
import sys
import datetime
import time
import multiprocessing


def download():
    cmd = 'streamlink --hls-live-restart -o {} {} best'.format(
        'cars.mp4', 'https://www.youtube.com/watch?v=1EiC9bvVGnk')
    os.system('timeout 10s ' + cmd)
    print('timeout 10s ' + cmd)


def timer(seconds):
    time.sleep(seconds)
    sys.exit()


if __name__ == '__main__':
    download()
   # p = multiprocessing.Process(
    #    target=download, name="download", args=(filename, url))
    # p.start()
    # time.sleep(10)
    # p.terminate()
    # p.join()

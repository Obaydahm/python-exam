import threading
import os
import sys
import datetime
import time
import multiprocessing


def download(filename, url):
    cmd = 'streamlink --hls-live-restart -o {} {} best'.format(
        filename, url)
    os.system(cmd)


def timer(seconds):
    time.sleep(seconds)
    sys.exit()


if __name__ == '__main__':
    url = sys.argv[1]
    filename = sys.argv[2]
    download(filename, url)
   # p = multiprocessing.Process(
    #    target=download, name="download", args=(filename, url))
    # p.start()
    # time.sleep(10)
    # p.terminate()
    # p.join()

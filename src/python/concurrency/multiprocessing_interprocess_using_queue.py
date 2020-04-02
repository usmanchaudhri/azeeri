# thumbnail_maker.py
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve

from queue import Queue
from threading import Thread
import multiprocessing

import PIL
from PIL import Image

"""
Example of using JoinableQueue as an inter-process communication mechanism.
And on how to share state inter-processes.

The program performs the following operations:
- performs an IO bound operation for downloading images uses Thread.
- performs a CPU bound operation for resizing images uses multiprocessing module.
- both the IO and CPU bound operations communicate with each other via JoinableQueue() or Queue()
"""

FORMAT = "[%(threadName)s, %(asctime), %(levelname)s] %(message)s"
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format=FORMAT)

class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.img_queue = multiprocessing.JoinableQueue()

    def download_image(self, dl_queue):
        while not dl_queue.empty():
            try:
                url = dl_queue.get(block=False)

                # download each image and save to the input dir
                img_filename = urlparse(url).path.split('/')[-1]
                urlretrieve(url, self.input_dir + os.path.sep + img_filename)
                self.img_queue.put(img_filename)

                dl_queue.task_done()

            except Queue.Empty:
                logging.info("Queue empty")

    def perform_resizing(self):
        # validate inputs
        if not os.listdir(self.input_dir):
            return
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        for filename in os.listdir(self.input_dir):
            orig_img = Image.open(self.input_dir + os.path.sep + filename)
            for basewidth in target_sizes:
                img = orig_img
                # calculate target height of the resized image to maintain the aspect ratio
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                # perform resizing
                img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)

                # save the resized image to the output dir with a modified file name
                new_filename = os.path.splitext(filename)[0] + \
                               '_' + str(basewidth) + os.path.splitext(filename)[1]
                img.save(self.output_dir + os.path.sep + new_filename)

            os.remove(self.input_dir + os.path.sep + filename)
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))


    def resize_image(self, filename):
        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        for filename in os.listdir(self.input_dir):
            orig_img = Image.open(self.input_dir + os.path.sep + filename)
            for basewidth in target_sizes:
                img = orig_img
                # calculate target height of the resized image to maintain the aspect ratio
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                # perform resizing
                img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)

                # save the resized image to the output dir with a modified file name
                new_filename = os.path.splitext(filename)[0] + \
                               '_' + str(basewidth) + os.path.splitext(filename)[1]
                img.save(self.output_dir + os.path.sep + new_filename)

            os.remove(self.input_dir + os.path.sep + filename)
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        pool =  multiprocessing.Pool()


        # instead of defining it globally we want to ensure that the
        # function is pickable which is why we would define the Queue here
        dl_queue = Queue()

        for img_url in img_url_list:
            dl_queue.put(img_url)

        # download images is IO bound
        num_dl_threads = 4
        for _ in range(num_dl_threads):
            t = Thread(target=self.download_image, args=(dl_queue,))
            t.start()

        # resize images which is CPU bound. For launching multiple processes to launch
        num_processes = multiprocessing.cpu_count()
        for _ in range(num_processes):
            p = multiprocessing.Process(target=self.perform_resizing)
            p.start()

        dl_queue.join()

        # to terminate all processes
        for _ in range(num_processes):
            self.img_queue.put(None)

        start_resize = time.perf_counter()
        pool.map(self.resize_image, self.img_list)              # both the target function and args should be picklable
        end_resize = time.perf_counter()

        pool.close()
        pool.join()

        logging.info("created {} thumbnails in {} seconds"  .format(len(self.img_list), end_resize - start_resize))






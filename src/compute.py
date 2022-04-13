import os
import glob
import json
from PIL import Image
import numpy as np
import cv2
from convert import string2image, image2string
from show_info import *

def compute_func(job_dir):
    for dir in glob.glob(f'{job_dir}/*'):
        job = os.path.basename(dir)
        if os.path.exists(f'{job_dir}/{job}/output.json') or os.path.exists(f'{job_dir}/{job}/computing'):
            continue
        else:
            with open(f'{job_dir}/{job}/computing', 'w') as f:
                f.write('')
            with open(f'{job_dir}/{job}/node', 'w') as f:
                f.write(show_mac())
            # execution
            input_dict = json.load(open(f'{job_dir}/{job}/input.json'))
            image_string = input_dict['Image']
            image = string2image(image_string)
            # pil to cv2
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            # compute algorithm
            image = cv2.resize(image, (512, 512))
            # cv2 to pil
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            image_string = image2string(image)
            output_dict = {'Image': image_string}
            with open(f'{job_dir}/{job}/output.json', 'w') as f:
                json.dump(output_dict, f)
            os.remove(f'{job_dir}/{job}/computing')
            break
if __name__ == '__main__':
    job_dir = '/share_db/job'
    device_dir = '/share_db/device'
    while True:
        save_info(device_dir)
        compute_func(job_dir)
        time.sleep(60)
    mac = show_mac()
    if os.path.exists(f'{device_dir}/{mac}'):
        os.remove(f'{device_dir}/{mac}')
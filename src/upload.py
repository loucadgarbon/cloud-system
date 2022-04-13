import os
import pandas as pd
import json
import uuid
from PIL import Image
from convert import image2string

def load_image(image_file):
    img = Image.open(image_file)
    return img
def create_job(image, filename, image_size, job_dir):
    job_id = uuid.uuid4()
    image_string = image2string(image)
    job_dict = {"Image": image_string, "Filename":filename, "ImageSize":image_size}
    os.makedirs(os.path.join(job_dir, str(job_id)))
    with open(os.path.join(job_dir, str(job_id), 'input.json'), 'w') as f:
        json.dump(job_dict, f)
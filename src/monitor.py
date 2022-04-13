import os
import json
import glob
import shutil
import pandas as pd
def create_device_table(device_dir):
    df = pd.DataFrame(columns=['Device', 'CPUUsage'])
    for file in glob.glob(f'{device_dir}/*'):
        device = os.path.basename(file)
        with open(f'{device_dir}/{device}') as f:
            cpu_usage = f.read()
        row_df = pd.DataFrame([[device, cpu_usage]], columns=['Device', 'CPUUsage'])
        df = pd.concat([df, row_df])
    df = df.reset_index(drop=True)
    return df
def create_job_table(job_dir):
    df = pd.DataFrame(columns=['Filename', 'ImageSize', 'JobID', 'ComputingNode', 'Status'])
    for dir in glob.glob(f'{job_dir}/*'):
        job = os.path.basename(dir)
        input_dict = json.load(open(f'{job_dir}/{job}/input.json'))
        filename = input_dict["Filename"]
        image_size = input_dict["ImageSize"]
        if os.path.exists(f'{job_dir}/{job}/computing'):
            status = '計算中'
            with open(f'{job_dir}/{job}/node') as f:
                node = f.read()
        elif os.path.exists(f'{job_dir}/{job}/output.json'):
            status = '已完成'
            with open(f'{job_dir}/{job}/node') as f:
                node = f.read()
        else:
            status = '等待'
            node = ''
        row_df = pd.DataFrame([[filename, image_size, job, node, status]], columns=['Filename', 'ImageSize', 'JobID', 'ComputingNode', 'Status'])
        df = pd.concat([df, row_df])
    df = df.reset_index(drop=True)
    return df

def create_job_list(job_dir):
    job_list = []
    for dir in glob.glob(f'{job_dir}/*'):
        job = os.path.basename(dir)
        if os.path.exists(f'{job_dir}/{job}/output.json') or os.path.exists(f'{job_dir}/{job}/computing'):
            continue
        else:
            job_list.append(job)
    return job_list

def delete_job(job_dir, del_job):
    for job in del_job:
        shutil.rmtree(f'{job_dir}/{job}')
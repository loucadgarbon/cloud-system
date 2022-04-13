from upload import *
from monitor import *

import streamlit as st
import glob



if __name__ == '__main__':
    job_dir = '/share_db/job'
    device_dir = '/share_db/device'
    os.makedirs(job_dir, exist_ok=True)
    os.makedirs(device_dir, exist_ok=True)
    image_file = st.file_uploader("選擇檔案", type=["jpg", "jpeg"])
    btn = st.button('上傳')
    if image_file is not None and btn:
        image = load_image(image_file)
        create_job(image, image_file.name, image_file.size, job_dir)
    st.title('工作管理員')
    st.header('設備狀態')
    st.dataframe(create_device_table(device_dir))
    st.header('工作狀態')
    st.dataframe(create_job_table(job_dir))
    del_job = st.multiselect('選擇要刪除的工作ID', create_job_list(job_dir))
    if st.button('刪除工作'):
        delete_job(job_dir, del_job)

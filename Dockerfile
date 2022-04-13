FROM ubuntu:latest
RUN apt update && apt install python3.8 python3-pip -y
RUN pip3 install streamlit pandas ipykernel opencv-python-headless black
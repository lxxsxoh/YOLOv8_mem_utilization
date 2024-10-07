import psutil
import os
from ultralytics import YOLO
from glob import glob
import matplotlib.pyplot as plt

def get_memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 ** 2) 

mem_usage_before_model_load = get_memory_usage()
print(f"Before loading model - Memory usage: {mem_usage_before_model_load:.2f} MB")

model = YOLO("yolov8n-obb.pt", task='obb')
tensorrt_model = YOLO("yolov8n-obb.engine", task='obb')
model.to("cpu")

image_paths = glob("./dota_images/*.png")

memory_usage = []  

mem_usage_before = get_memory_usage()
print(f"Before starting inference - Memory usage: {mem_usage_before:.2f} MB")

for i, image_path in enumerate(image_paths):
    result = tensorrt_model(image_path)
    mem_usage = get_memory_usage()
    memory_usage.append(mem_usage)
    print(f"Processed image {i+1}/{len(image_paths)} - Memory usage: {mem_usage:.2f} MB")
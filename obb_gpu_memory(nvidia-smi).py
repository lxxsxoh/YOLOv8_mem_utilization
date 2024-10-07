import os
from ultralytics import YOLO
from glob import glob
import subprocess

def get_gpu_memory_usage():
    result = subprocess.run(['nvidia-smi', '--query-gpu=memory.used', '--format=csv,nounits,noheader'], stdout=subprocess.PIPE)
    mem_usage = float(result.stdout.decode('utf-8').strip())  # 메모리 사용량(MB 단위)
    return mem_usage

mem_usage_before_model_load = get_gpu_memory_usage()
print(f"Before loading model - GPU Memory usage: {mem_usage_before_model_load:.2f} MB")

model = YOLO("yolov8n-obb.pt", task='obb')
tensorrt_model = YOLO("yolov8n-obb.engine", task='obb')
model.to("cpu")

image_paths = glob("./dota_images/*.png")

memory_usage = []

mem_usage_before = get_gpu_memory_usage()
print(f"Before starting inference - GPU Memory usage: {mem_usage_before:.2f} MB")

for i, image_path in enumerate(image_paths):
    result = tensorrt_model(image_path)
    mem_usage = get_gpu_memory_usage() 
    memory_usage.append(mem_usage)
    print(f"Processed image {i+1}/{len(image_paths)} - GPU Memory usage: {mem_usage:.2f} MB")

#!/bin/bash

if [ ! -d "gpu_results" ]; then
    mkdir gpu_results
else
    rm -f gpu_results/*.txt
fi

if [ ! -d "memory_results" ]; then
    mkdir memory_results
else
    rm -f memory_results/*.txt
fi

monitor_gpu() {
    local script_name=$1
    local gpu_file="gpu_results/${script_name%.py}_gpu.txt"
    local result_file="memory_results/${script_name%.py}_result.txt"

    while true; do
        nvidia-smi --query-gpu=utilization.gpu,utilization.memory --format=csv >> $gpu_file
        sleep 1
    done &
    NVIDIA_SMI_PID=$!

    python3 $script_name > $result_file

    kill $NVIDIA_SMI_PID
}

monitor_gpu "obb_gpu_memory.py"
monitor_gpu "pose_gpu_memory.py"
monitor_gpu "detect_gpu_memory.py"
monitor_gpu "classify_gpu_memory.py"
monitor_gpu "segment_gpu_memory.py"

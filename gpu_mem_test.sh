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
    local result_file="memory_results/${script_name%.py}_memory_result.txt"

    (tegrastats --interval 5000 | grep --line-buffered -oP 'GR3D_FREQ \K\d+%@\[\d+\]' > $gpu_file) &
    TEGRA_PID=$!

    python3 $script_name > $result_file

    kill $TEGRA_PID
}

monitor_gpu "obb_memory.py"
monitor_gpu "pose_memory.py"
monitor_gpu "detect_memory.py"
monitor_gpu "classify_memory.py"
monitor_gpu "segment_memory.py"
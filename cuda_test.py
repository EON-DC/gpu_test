import os
# docker run --gpus all -v /app gpu_test python cuda_test.py
from tensorflow.python.client import device_lib


print(device_lib.list_local_devices())
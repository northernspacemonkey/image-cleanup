# ====================================================================================================
# _  _ ____ ____ ___ _  _ ____ ____ _  _    ____ ___  ____ ____ ____    _  _ ____ _  _ _  _ ____ _   _ 
# |\ | |  | |__/  |  |__| |___ |__/ |\ |    [__  |__] |__| |    |___    |\/| |  | |\ | |_/  |___  \_/  
# | \| |__| |  \  |  |  | |___ |  \ | \|    ___] |    |  | |___ |___    |  | |__| | \| | \_ |___   |   
# ====================================================================================================
#
# Python Image Functions
# Noise Reduction Routine
# Includes CPU benchmarking output routines that can be optionally switched on.
# 
# Operation: python3 ./edgedetect_grayscale.py MYIMAGE {CPU}
#
# If you want CPU Benchmarking output, add the optional CPU flag after the image name.

import time
import multiprocessing as mp
import psutil
import sys

from PIL import Image, ImageFilter

IMAGENAME = ""
# Get the Image name
if len(sys.argv)>1:
    IMAGENAME = sys.argv[1]

if IMAGENAME == "":
    print("Missing Image to Manipulate")
    exit(1)

# Check to see if you want CPU Benchmarking output
CPUFLAG = 0
if len(sys.argv)>2:
    if sys.argv[2]=="CPU":
        CPUFLAG = 1
    

# Primary Manipualtion Routine
def despeckle():
    # Open the source image
    input_image = Image.open(IMAGENAME)
    # Apply a Gaussian blur to the open image
    output_image = input_image.filter(ImageFilter.BoxBlur(3))
    # Save the output to a file
    OUTPUTIMAGE = "OUTPUT_" + IMAGENAME
    output_image.save(OUTPUTIMAGE)

# CPU Monitoring Routine
def monitor_process(target):
    # Set up the worker process
    worker_process = mp.Process(target=target)
    worker_process.start()
    p = psutil.Process(worker_process.pid)
    # Log CPU usage every 10 milliseconds
    cpu_percents = []
    # While the process is ongoing get the cpu value
    while worker_process.is_alive():
        cpu_percents.append(p.cpu_percent())
        time.sleep(0.01)
    
    worker_process.join()
    return cpu_percents

if CPUFLAG==1:
    cpu_percents = monitor_process(target=despeckle)
    # Output the CPU values for the duration of the process period
    print(cpu_percents)
    exit(0)
else:
    despeckle
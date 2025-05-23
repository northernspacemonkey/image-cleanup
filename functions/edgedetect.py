# ====================================================================================================
# _  _ ____ ____ ___ _  _ ____ ____ _  _    ____ ___  ____ ____ ____    _  _ ____ _  _ _  _ ____ _   _ 
# |\ | |  | |__/  |  |__| |___ |__/ |\ |    [__  |__] |__| |    |___    |\/| |  | |\ | |_/  |___  \_/  
# | \| |__| |  \  |  |  | |___ |  \ | \|    ___] |    |  | |___ |___    |  | |__| | \| | \_ |___   |   
# ====================================================================================================
#
# Python Image Functions
# Heavy Edge Detection Routine
# Includes CPU benchmarking output routines that can be optionally switched on.
# 
# Operation: python3 ./edgedetect_heavy.py MYIMAGE {CPU}
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
def edgedetect():
    # Open the source image
    input_image = Image.open(IMAGENAME)
    output_image = input_image.filter(ImageFilter.BoxBlur(3))
    output_image = output_image.convert("RGBA")
    # Convert to a gray-scale imager and smooth the image to help edge detection
    output_image = output_image.filter(ImageFilter.SMOOTH)
    output_image = output_image.filter(ImageFilter.CONTOUR)
    # Map white to transparent
    imagedata = output_image.load()
    width, height = output_image.size
    for y in range(height):
      for x in range(width):
        if imagedata[x, y] == (255, 255, 255, 255):
            imagedata[x, y] = (255, 255, 255, 0)
    # Create Composit Image using the original plus the modified version
    composite_image = Image.alpha_composite(input_image, output_image)
    # Save the composite output to a file
    OUTPUTIMAGE = "OUTPUT_" + IMAGENAME
    composite_image.save(OUTPUTIMAGE)

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
    cpu_percents = monitor_process(target=edgedetect)
    # Output the CPU values for the duration of the process period
    print(cpu_percents)
    exit(0)
else:
    edgedetect

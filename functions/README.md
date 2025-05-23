# Python Image Library Functions

Several routines that can be used to modify base imagery and produce useful output.

Run each with the format:

```python3 functionFile.py MYFILENAME {CPU}```

Where the optional CPU flag allows the output of processor benchmark utilisation for the function time-sliced every 10ms.

# Output

Sample output using a primary source image of cloud data over Europe. As expected, function output varies depending on the source imagery and can lead to different results depending on the source.

## Primary Source Image:

![Source Image](./source_images/worldWeather1.png)

## Edge Detect : GrayScale

![Edge Detect Grayscale](./output_images/EDG_OUTPUT_worldWeather1.png)

## Edge Detect : Heavy Edge

![Edge Detect Heavy Edges](./output_images/ED_OUTPUT_worldWeather1.png)

## Noise Reduction

![Noise Reduction](./output_images/NR_OUTPUT_worldWeather1.png)

## Thumbnail

![Thumbnail Resampling](./output_images/THUMB_OUTPUT_worldWeather1.png)


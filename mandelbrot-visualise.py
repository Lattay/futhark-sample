#!/usr/bin/env python

from PIL import Image
import numpy
from mandelbrot import mandelbrot

m = mandelbrot()

filename = "mandelbrot.png"
width = 800
height = 600
limit = 255
minx = -2.23
miny = -1.15
maxx = 0.83
maxy = 1.15
# The .get() is to obtain a Numpy array instead of a PyOpenCL array.
fut_image = m.main(width, height, limit, minx, miny, maxx, maxy).get()

# Futhark gives us an array of 32-bit integers encoding the color,
# but the PNG writer expects each colour channel to be separate.
image = numpy.empty((height, width, 3), dtype="uint8")
image[:, :, 0] = (fut_image & 0xFF0000) >> 16
image[:, :, 1] = (fut_image & 0xFF00) >> 8
image[:, :, 2] = fut_image & 0xFF

img = Image.fromarray(image)
img.save(filename)

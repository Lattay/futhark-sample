# Futhark + PyOpenCL example

This repository contains an example of using Futhark with PyOpenCL, Numpy and Pillow to compute an image on the GPU.

## Install

You will need to install [Futhark](https://futhark-lang.org/), [PyOpenCL](https://pypi.org/project/pyopencl/), [Numpy](https://pypi.org/project/numpy/) and [Pillow](https://pypi.org/project/Pillow/), as well as a OpenCL compatible platform.
If you have a Nvidia GPU it would be CUDA, opencl-mesa for AMD and I recommend [PoCL](http://portablecl.org/) for Intel GPU.

## Usage

Simply `$ make`.
Have a look in the [Makefile](./Makefile) to see what is happening. It is dead simple.

The result of running make is the `mandelbrot.py` file generated by the `futhark` compiler and the [mandelbrot.png](./mandelbrot.png) image.

## Credit
The `mandelbrot.fut` file is directly taken from [Futhark website](https://futhark-lang.org/blog/2016-04-15-futhark-and-pyopencl.html) and the `mandelbrot-visualise.py` is only slightly modified to use Pillow to create a PNG.
All credits goes to the Futhark authors and [DIKU](https://di.ku.dk/)

mandelbrot.png: mandelbrot.py mandelbrot-visualise.py
	python mandelbrot-visualise.py

mandelbrot.py: mandelbrot.fut
	futhark pyopencl --library mandelbrot.fut

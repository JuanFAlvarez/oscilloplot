import numpy as np
import imageio
# this script takes an image, turns it to black and white and gets the points of the white pixels
# oscilloscope will plot all white pixels 

# load image
tesla = imageio.imread('tesla255invert.png')

# turn it into black and white
tesla_bw= tesla[..., 0] > 127

# extract white pixel coordinates and correct order of x,y to be used in arduino plotter
white_coords = np.argwhere(tesla_bw)
white_coords = np.flip(white_coords,1)

# save as .csv or .txt as pure coordinate points to be processed by trimpoints.py
np.savetxt('tesla.txt', white_coords, fmt='%d', delimiter=',')

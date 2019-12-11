import os
import numpy
from PIL import Image

input_file_name = os.path.normpath(os.path.join(os.path.abspath(__file__), '../input/8_image.txt'))
with open(input_file_name, 'r') as pgm_file:
    pixellist = [int(x) for x in str(pgm_file.readline().strip('\n'))]

# Part 1:
n_pixels = len(pixellist)
n_cols = 25
n_rows = 6
assert(n_pixels % (n_cols*n_rows) == 0)
n_layers = int(n_pixels/(n_cols*n_rows))
layered_image = numpy.reshape(pixellist, (n_layers, n_rows, n_cols))
min_zeros = n_cols*n_rows+1
for i_layer in range(n_layers):
    unique, counts = numpy.unique(layered_image[i_layer], return_counts=True)
    occurances = dict(zip(unique, counts))
    if(occurances[0] < min_zeros):
        min_zeros = occurances[0]
        output = occurances[1]*occurances[2]
print(output)

# Part 2:
image = numpy.ndarray((n_rows, n_cols))
for i_row in range(n_rows):
    for i_col in range(n_cols):
        layered_pixel = layered_image[:, i_row, i_col]
        image[i_row, i_col] = layered_pixel[numpy.nonzero(2-layered_pixel)][0]
Image.fromarray(255*image).show()

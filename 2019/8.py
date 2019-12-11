import os

input_file_name = os.path.normpath(os.path.join(os.path.abspath(__file__), '../input/8_image.txt'))
with open(input_file_name, 'r') as pgm_file:
    pixellist = [int(x) for x in pgm_file.readline().strip('\n')]

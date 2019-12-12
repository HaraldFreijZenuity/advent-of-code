import itertools
import intcode
import os
input_file_name = os.path.normpath(os.path.join(os.path.abspath(__file__), '../input/9_program.txt'))
with open(input_file_name, 'r') as pgm_file:
    program = [int(x) for x in pgm_file.readline().strip('\n').split(',')]
output = intcode.intcode(program, input_values=[1])
print(output)
output = intcode.intcode(program, input_values=[2])
print(output)

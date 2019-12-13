import os
import numpy
import intcode
from PIL import Image


def run_robot(program, start_color):
    pos = [0, 0]
    direction = UP
    curr_pos = 0
    offset_base = 0
    panel = {}
    panel[tuple(pos)] = start_color
    while True:
        # Check color and run program
        if tuple(pos) not in panel.keys():
            panel[tuple(pos)] = BLACK
        color = panel[tuple(pos)]
        output, curr_pos, stop_reason, offset_base = intcode.intcode(program, curr_pos, offset_base, [color])
        # Paint
        panel[tuple(pos)] = output[0]
        # Move
        if output[1] == 1:
            direction = (direction + 1) % 4
        elif output[1] == 0:
            direction = (direction - 1) % 4
        else:
            print("Invalid direction output!")
            assert False
        if direction == UP:
            pos[0] -= 1
        elif direction == DOWN:
            pos[0] += 1
        elif direction == LEFT:
            pos[1] -= 1
        elif direction == RIGHT:
            pos[1] += 1
        else:
            print("Invalid direction stored!")
            assert False
        if stop_reason == intcode.HALTED:
            break
    return panel


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
BLACK = 0
WHITE = 1
# initiale robot
input_file_name = os.path.normpath(os.path.join(os.path.abspath(__file__), '../input/11_program.txt'))
with open(input_file_name, 'r') as pgm_file:
    program = [int(x) for x in pgm_file.readline().strip('\n').split(',')]
# Part 1
panel = run_robot(program.copy(), BLACK)
print(len(panel))
# Part 2
panel = run_robot(program.copy(), WHITE)
panel_mx = numpy.zeros((60, 60))
for p in panel.keys():
    panel_mx[p] = panel[p]
Image.fromarray(255*panel_mx).show()

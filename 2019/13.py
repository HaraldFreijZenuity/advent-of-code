import intcode
import os
import numpy
import sys
import termios
import tty
import pygame
from PIL import Image


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


input_file_name = os.path.normpath(os.path.join(os.path.abspath(__file__), '../input/13_program.txt'))
with open(input_file_name, 'r') as pgm_file:
    program = [int(x) for x in pgm_file.readline().strip('\n').split(',')]

# Part 1
board = numpy.zeros((100, 100))
output, curr_pos, stop_reason, offset_base = intcode.intcode(program.copy(), 0, 0, [])
assert(stop_reason) == intcode.HALTED
for i in range(0, len(output), 3):
    board[output[i], output[i+1]] = output[i+2]
while (board[:, -1] == 0).all():
    board = numpy.delete(board, board.shape[1]-1, 1)
while (board[-1, :] == 0).all():
    board = numpy.delete(board, board.shape[0]-1, 0)
unique, counts = numpy.unique(board, return_counts=True)
print(dict(zip(unique, counts))[2])
Image.fromarray(255*board/board.max()).show()

# Part 2
program[0] = 2
board = numpy.zeros((100, 100))
output, curr_pos, stop_reason, offset_base = intcode.intcode(program, 0, 0, [])
assert(stop_reason) == intcode.WAITING
for i in range(0, len(output), 3):
    board[output[i], output[i+1]] = output[i+2]
while (board[:, -1] == 0).all():
    board = numpy.delete(board, board.shape[1]-1, 1)
while (board[-1, :] == 0).all():
    board = numpy.delete(board, board.shape[0]-1, 0)

while stop_reason == intcode.WAITING:
    char = getch()
    if char == "a":
        direction = -1
    elif char == "d":
        direction = 1
    else:
        direction = 0
    output, curr_pos, stop_reason, offset_base = intcode.intcode(
        program, curr_pos=curr_pos, offset_base=offset_base, input_values=[direction])
    image = Image.fromarray(255*board/board.max())
    image.resize(imageshow()


unique, counts=numpy.unique(board, return_counts=True)
print(dict(zip(unique, counts))[2])
Image.fromarray(255*board/board.max()).resshow()

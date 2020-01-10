import intcode
import os
import numpy
import sys

input_file_name = os.path.normpath(os.path.join(os.path.abspath(__file__), '../input/15_program.txt'))
with open(input_file_name, 'r') as pgm_file:
    program = [int(x) for x in pgm_file.readline().strip('\n').split(',')]

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4
WALL = 0
EMPTY = 1
OXYGEN = 2


def back(dir):
    if dir == NORTH:
        return SOUTH
    if dir == SOUTH:
        return NORTH
    if dir == WEST:
        return EAST
    if dir == EAST:
        return WEST


def step(dir):
    if dir == NORTH:
        return numpy.array([1, 0])
    if dir == SOUTH:
        return numpy.array([-1, 0])
    if dir == WEST:
        return numpy.array([0, -1])
    if dir == EAST:
        return numpy.array([0, 1])


def investigate(distances, pos, best_distance, program, curr_pgm_pos, offset_base):
    d = distances[pos]
    for direction in [NORTH, SOUTH, EAST, WEST]:
        output, curr_pgm_pos, stop_reason, offset_base = intcode.intcode(
            program, curr_pos=curr_pgm_pos, offset_base=offset_base, input_values=[direction])
        assert len(output) == 1
        if not output[0] == WALL:
            new_pos = tuple(numpy.array(pos)+step(direction))
            if new_pos not in distances or d+1 < distances[new_pos]:
                distances[new_pos] = d+1
                if output == OXYGEN:
                    print("OXYGEN!!!!")
                    best_distance = distances[new_pos]
                else:
                    best_distance = min(best_distance, investigate(
                        distances, new_pos, best_distance, program, curr_pgm_pos, offset_base))
            output, curr_pgm_pos, stop_reason, offset_base = intcode.intcode(
                program, curr_pos=curr_pgm_pos, offset_base=offset_base, input_values=[back(direction)])
            assert len(output) == 1
            assert(output[0] == EMPTY)
    return best_distance


distances = {}
pos = (0, 0)
distances[pos] = 0
print("Distance to oxygen: {}".format(investigate(distances, pos, 10000000, program, 0, 0)))

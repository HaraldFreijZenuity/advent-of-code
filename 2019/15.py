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


def print_board(distances):
    numpy.set_printoptions(threshold=sys.maxsize)
    numpy.set_printoptions(linewidth=200)
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    for pos in distances:
        x_min = min(x_min, pos[0])
        x_max = max(x_max, pos[0])
        y_min = min(y_min, pos[1])
        y_max = max(y_max, pos[1])
    board = numpy.zeros((x_max-x_min+1, y_max-y_min+1))
    for pos in distances:
        board[(pos[0]-x_min, pos[1]-y_min)] = distances[pos]
    print(board)


def find_oxygen(distances, pos, best_distance, program, curr_pgm_pos, offset_base):
    d = distances[pos]
    for direction in [NORTH, SOUTH, EAST, WEST]:
        output, curr_pgm_pos, stop_reason, offset_base = intcode.intcode(
            program, curr_pos=curr_pgm_pos, offset_base=offset_base, input_values=[direction])
        assert len(output) == 1
        if not output[0] == WALL:
            new_pos = tuple(numpy.array(pos)+step(direction))
            if new_pos not in distances or d+1 < distances[new_pos]:
                distances[new_pos] = d+1
                if output[0] == OXYGEN:
                    best_distance = distances[new_pos]
                    oxygen_distances = {new_pos: 0}
                    find_deepest(oxygen_distances, new_pos, program, curr_pgm_pos, offset_base)
                    print("Time for oxygen filling: {}".format(max(oxygen_distances.values())))
                else:
                    best_distance = min(best_distance, find_oxygen(
                        distances, new_pos, best_distance, program, curr_pgm_pos, offset_base))
            output, curr_pgm_pos, stop_reason, offset_base = intcode.intcode(
                program, curr_pos=curr_pgm_pos, offset_base=offset_base, input_values=[back(direction)])
            assert len(output) == 1
            assert(output[0] == EMPTY)
    return best_distance


def find_deepest(distances, pos, program, curr_pgm_pos, offset_base):
    d = distances[pos]
    for direction in [NORTH, SOUTH, EAST, WEST]:
        output, curr_pgm_pos, stop_reason, offset_base = intcode.intcode(
            program, curr_pos=curr_pgm_pos, offset_base=offset_base, input_values=[direction])
        assert len(output) == 1
        if not output[0] == WALL:
            new_pos = tuple(numpy.array(pos)+step(direction))
            if new_pos not in distances or d+1 < distances[new_pos]:
                distances[new_pos] = d+1
                find_deepest(distances, new_pos, program, curr_pgm_pos, offset_base)
            output, curr_pgm_pos, stop_reason, offset_base = intcode.intcode(
                program, curr_pos=curr_pgm_pos, offset_base=offset_base, input_values=[back(direction)])
            assert len(output) == 1
            assert not output[0] == WALL


print("Distance to oxygen: {}".format(find_oxygen({(0, 0): 0}, (0, 0), 10000000, program.copy(), 0, 0)))

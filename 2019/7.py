import itertools
import intcode
import os
input_file_name = os.path.normpath(os.path.join(os.path.abspath(__file__), '../input/7_program.txt'))
with open(input_file_name, 'r') as pgm_file:
    program = [int(x) for x in pgm_file.readline().strip('\n').split(',')]

n_amplifiers = 5
# Part 1
max_out = 0
for perm in itertools.permutations(range(n_amplifiers)):
    input_val = 0
    for i in range(n_amplifiers):
        output, curr_pos, stop_reason, offset_base = intcode.intcode(
            program=program.copy(), input_values=[perm[i], input_val])
        input_val = output[0]
    max_out = max(max_out, output[0])
print('Answer 1: {}'.format(max_out))

# Part 2
max_out = 0
for perm in itertools.permutations(range(n_amplifiers, 2*n_amplifiers)):
    programs = [program.copy() for i in range(n_amplifiers)]
    positions = [0]*n_amplifiers
    offset_bases = [0]*n_amplifiers
    inputs = [[perm[i]] for i in range(n_amplifiers)]
    inputs[0].append(0)
    n = 0
    for i in itertools.cycle(range(n_amplifiers)):
        n += 1
        (outputs, positions[i], stop_reason, offset_bases[i]) = intcode.intcode(
            programs[i], curr_pos=positions[i], input_values=inputs[i], offset_base=offset_bases[i])
        if (i == n_amplifiers-1):
            thruster_out = outputs[0]
            if(stop_reason == intcode.HALTED):
                break
        inputs[i] = []
        inputs[(i+1) % n_amplifiers].append(outputs[0])
    max_out = max(max_out, thruster_out)
print('Answer 2: {}'.format(max_out))

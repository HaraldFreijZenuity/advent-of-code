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
    input = 0
    for i in range(n_amplifiers):
        outputs = intcode.intcode(program.copy(), input_values=[perm[i], input])
        input = outputs[0]
    max_out = max(max_out, outputs[0])
print(max_out)

# Part 2
max_out = 0
for perm in itertools.permutations(range(n_amplifiers, 2*n_amplifiers)):
    programs = [program.copy() for i in range(n_amplifiers)]
    positions = [0]*n_amplifiers
    inputs = [[perm[i]] for i in range(n_amplifiers)]
    inputs[0].append(0)
    n = 0
    for i in itertools.cycle(range(n_amplifiers)):
        n += 1
        (positions[i], outputs, stop_reason) = intcode.intcode(
            programs[i], curr_pos=positions[i], input_values=inputs[i])
        if (i == n_amplifiers-1):
            thruster_out = outputs[0]
            if(stop_reason == intcode.HALTED):
                break
        inputs[i] = []
        inputs[(i+1) % n_amplifiers].append(outputs[0])
    max_out = max(max_out, thruster_out)
print(max_out)

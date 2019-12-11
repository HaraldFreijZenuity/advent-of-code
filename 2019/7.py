import itertools
import intcode
with open("input/7_program.txt", 'r') as pgm_file:
    program = [int(x) for x in pgm_file.readline().strip('\n').split(',')]

program = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
           27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
# program = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
#            -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
#            53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]
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
    programs = [program for i in range(n_amplifiers)]
    positions = [0]*n_amplifiers
    inputs = [[perm[i]] for i in range(n_amplifiers)]
    inputs[0].append(0)
    for i in itertools.cycle(range(n_amplifiers)):
        print('Running program {} with input {}'.format(i, inputs[i]))
        (positions[i], outputs, stop_reason) = intcode.intcode(
            programs[i], curr_pos=positions[i], input_values=inputs[i])
        print('Stopping for reason {} at {} with outputs {}'.format(stop_reason, positions[i], outputs))
        if (i == 4):
            thruster_out = outputs[0]
        if(stop_reason == intcode.HALTED):
            break
        inputs[i] = []
        inputs[(i+1) % n_amplifiers].append(outputs[0])
    max_out = max(max_out, thruster_out)
print(max_out)

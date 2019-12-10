import itertools
import intcode
with open("input/7_program.txt", 'r') as pgm_file:
    program = [int(x) for x in pgm_file.readline().strip('\n').split(',')]

n_amplifiers = 5
max_out = 0
for perm in itertools.permutations(range(n_amplifiers)):
    input = 0
    for i in range(n_amplifiers):
        outputs = intcode.intcode(program.copy(), [perm[i], input])
        input = outputs[0]
    max_out = max(max_out, outputs[0])
print(max_out)

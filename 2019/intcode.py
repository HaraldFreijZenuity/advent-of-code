import numpy

n_parameters = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
instruction_lengths = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]
instructions = ['', '+', '*', 'input', 'output', 'jump-if-true', 'jump-if-false', 'less than', 'equals']
HALTED = 0
WAITING = 1


###
# Runs an intcode program, and returns output, curr_pos, stop_reason, offset_base
def intcode(program, curr_pos=0, offset_base=0, input_values=None):
    if input_values is None:
        input_values = []
    input_pos = 0
    output = []
    stop_reason = None
    while(True):
        instruction = program[curr_pos]
        (opcode, modes) = parse_instruction(instruction)
        if(opcode == 99):
            stop_reason = HALTED
            break
        inst_pos = []
        for i in range(n_parameters[opcode]):
            if (modes[i] == 0):
                inst_pos.append(program[curr_pos+i+1])
            elif(modes[i] == 1):
                inst_pos.append(curr_pos+i+1)
            elif(modes[i] == 2):
                inst_pos.append(program[curr_pos+i+1]+offset_base)
            else:
                print('Error! Invalid mode!')
                assert false
        for p in inst_pos:
            if p >= len(program):
                program.extend([0]*(p-len(program)+1))
        if (opcode == 1):  # Addition
            program[inst_pos[2]] = program[inst_pos[0]] + program[inst_pos[1]]
        elif(opcode == 2):  # Multiplication
            program[inst_pos[2]] = program[inst_pos[0]] * program[inst_pos[1]]
        elif(opcode == 3):  # Input
            if(input_pos >= len(input_values)):
                stop_reason = WAITING
                break
            program[inst_pos[0]] = input_values[input_pos]
            input_pos += 1
        elif(opcode == 4):  # Output
            output.append(program[inst_pos[0]])
        elif(opcode == 5):  # Jump-if-true
            if(program[inst_pos[0]] != 0):
                curr_pos = program[inst_pos[1]]-instruction_lengths[opcode]
        elif(opcode == 6):  # Jump-if-false
            if(program[inst_pos[0]] == 0):
                curr_pos = program[inst_pos[1]]-instruction_lengths[opcode]
        elif(opcode == 7):  # Less than
            program[inst_pos[2]] = 1 if program[inst_pos[0]] < program[inst_pos[1]] else 0
        elif(opcode == 8):  # Equals
            program[inst_pos[2]] = 1 if program[inst_pos[0]] == program[inst_pos[1]] else 0
        elif(opcode == 9):  # Offset
            offset_base += program[inst_pos[0]]
        else:
            print('Error! Invalid opcode!')
            assert false
        curr_pos += instruction_lengths[opcode]
    return output, curr_pos, stop_reason, offset_base


def parse_instruction(instruction):
    opcode = numpy.mod(instruction, 100)
    if(opcode == 99):
        return (opcode, [])
    modes = []
    for i in range(n_parameters[opcode]):
        modes.append(numpy.mod(int(instruction/(10**(i+2))), 10))
    return (opcode, modes)

import numpy

n_read_parameters = [0, 2, 2, 0, 1, 2, 2, 2, 2]
instruction_lengths = [0, 4, 4, 2, 2, 3, 3, 4, 4]
instructions = ['', '+', '*', 'input', 'output', 'jump-if-true', 'jump-if-false', 'less than', 'equals']


def intcode(program, input_values=None):
    if input_values is None:
        input_values = []
    curr_pos = 0
    input_pos = 0
    output = []
    while(True):
        instruction = program[curr_pos]
        (opcode, modes) = parse_instruction(instruction)
        if(opcode == 99):
            return output
        values = []
        for i in range(n_read_parameters[opcode]):
            if (modes[i] == 0):
                values.append(program[program[curr_pos+i+1]])
            elif(modes[i] == 1):
                values.append(program[curr_pos+i+1])
            else:
                print('Error! Invalid mode!')
                return
        if (opcode == 1):  # Addition
            program[program[curr_pos+3]] = values[0] + values[1]
        elif(opcode == 2):  # Multiplication
            program[program[curr_pos+3]] = values[0] * values[1]
        elif(opcode == 3):  # Input
            program[program[curr_pos+1]] = input_values[input_pos]
            input_pos += 1
        elif(opcode == 4):  # Output
            output.append(values[0])
        elif(opcode == 5):  # Jump-if-true
            if(values[0] != 0):
                curr_pos = values[1]-instruction_lengths[opcode]
        elif(opcode == 6):  # Jump-if-false
            if(values[0] == 0):
                curr_pos = values[1]-instruction_lengths[opcode]
        elif(opcode == 7):  # Less than
            program[program[curr_pos+3]] = 1 if values[0] < values[1] else 0
        elif(opcode == 8):  # Equals
            program[program[curr_pos+3]] = 1 if values[0] == values[1] else 0
        else:
            print('Error! Invalid opcode!')
            return
        curr_pos += instruction_lengths[opcode]


def parse_instruction(instruction):
    opcode = numpy.mod(instruction, 100)
    if(opcode == 99):
        return (opcode, [])
    modes = []
    for i in range(n_read_parameters[opcode]):
        modes.append(numpy.mod(int(instruction/(10**(i+2))), 10))
    return (opcode, modes)

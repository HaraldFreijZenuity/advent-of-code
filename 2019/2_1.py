original_program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]
done = False
for noun in range(100):
    for verb in range(100):
        print("Noun: {}, verb: {}".format(noun, verb))
        program=original_program.copy()
        program[1] = noun
        program[2] = verb
        curr_pos = 0

        while(True):
            if (program[curr_pos] == 1):
                program[program[curr_pos+3]] = program[program[curr_pos+1]] + \
                    program[program[curr_pos+2]]
            elif(program[curr_pos] == 2):
                program[program[curr_pos+3]] = program[program[curr_pos+1]] * \
                    program[program[curr_pos+2]]
            elif(program[curr_pos] == 99):
                print("Found return code. Position 0 value: {}".format(program[0]))
                break
            else:
                print("Error! Opcode {} at position {}".format(
                    program[curr_pos], curr_pos))
                break
            curr_pos += 4
        if (program[0]==19690720):
            print("Success!")
            done=True
            break
    if done: break

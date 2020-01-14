import os

input_file_name = os.path.normpath(os.path.join(os.path.abspath(__file__), '../input/16_input.txt'))
with open(input_file_name, 'r') as pgm_file:
    input_list = [int(x) for x in pgm_file.readline().strip('\n')]


def fft(input, pattern):
    output = [0]*len(input)
    for i_in in range(len(input)):
        for i_out in range(1, len(output)+1):
            # print(int((i_in+1)/i_out), end=',')
            # print(int((i_in+1)/i_out) % len(pattern), end=',')
            # print(pattern[int((i_in+1)/i_out) % len(pattern)], end='\t')
            output[i_out-1] += input[i_in]*pattern[int((i_in+1)/i_out) % len(pattern)]
        # print('')
    output = [abs(x) % 10 for x in output]
    # print('')
    return output


pattern = [0, 1, 0, -1]
for i in range(100):
    print(i)
    input_list = fft(input_list, pattern)
print(input_list[0:8])

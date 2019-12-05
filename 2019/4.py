import numpy
start = 231832
end = 767346
n_valid = 0
for n in range(start, end+1):
    n_list = [int(x) for x in str(n)]
    # if(all(i <= j for i, j in zip(n_list, n_list[1:])) and len({x for x in n_list}) != len(n_list)):
    if(all(i <= j for i, j in zip(n_list, n_list[1:])) and any(n_list.count(i) == 2 for i in n_list)):
        n_valid += 1
print(n_valid)

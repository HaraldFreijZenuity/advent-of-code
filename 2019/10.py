import numpy
import os
import itertools

input_file_name = os.path.normpath(os.path.join(os.path.abspath(__file__), '../input/10_map.txt'))
with open(input_file_name, 'r') as map_file:
    map_str = [x for x in map_file.read().split()]

meteors = []
r = 0
for line in map_str:
    c = 0
    for char in line:
        if char == '#':
            meteors.append((c, r))
        c += 1
    r += 1
stars_to_vaporize = {}
for s1 in meteors:
    stars_by_angle = {}
    for s2 in meteors:
        if(s1 != s2):
            dc = s2[0]-s1[0]
            dr = s2[1]-s1[1]
            angle = numpy.arctan2(dc, -dr)
            angle += 2*numpy.pi*(angle < 0)
            dist = numpy.sqrt(dc**2+dr**2)
            if (angle not in stars_by_angle.keys()):
                stars_by_angle[angle] = []
            stars_by_angle[angle].append((dist, s2))
    if (len(stars_by_angle) > len(stars_to_vaporize)):
        stars_to_vaporize = stars_by_angle
print(len(stars_to_vaporize))

n_vaporized = 0
for angle in itertools.cycle(sorted(stars_to_vaporize.keys())):
    stars_to_vaporize[angle].sort()
    if len(stars_to_vaporize[angle]) > 0:
        s = stars_to_vaporize[angle].pop(0)
        n_vaporized += 1
        if n_vaporized == 200:
            print(s)
            exit()

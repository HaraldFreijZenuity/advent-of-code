import numpy
import copy
import itertools
# <x=-2, y=9, z=-5>
# <x=16, y=19, z=9>
# <x=0, y=3, z=6>
# <x=11, y=0, z=11>
n_planets = 4
velocities = [numpy.array([0, 0, 0]) for i in range(n_planets)]
positions = []
positions.append(numpy.array([-2, 9, -5]))
positions.append(numpy.array([16, 19, 9]))
positions.append(numpy.array([0, 3, 6]))
positions.append(numpy.array([11, 0, 11]))

positions_original = copy.deepcopy(positions)
velocities_original = copy.deepcopy(velocities)

# # <x=-1 ,   y=0,   z=2>
# # <x=2 ,    y=-10, z=-7>
# # <x=4 ,    y=-8,  z=8>
# # <x=3 ,    y=5,   z=-1>
# positions = []
# positions.append(numpy.array([-1, 0,  2]))
# positions.append(numpy.array([2, -10, -7]))
# positions.append(numpy.array([4, -8, 8]))
# positions.append(numpy.array([3, 5,  -1]))


for i in range(1000):
    for pair in itertools.combinations(range(n_planets), 2):
        for c in range(3):
            d = bool(positions[pair[0]][c] < positions[pair[1]][c])-bool(positions[pair[1]][c] < positions[pair[0]][c])
            velocities[pair[0]][c] += d
            velocities[pair[1]][c] -= d
    for p in range(n_planets):
        positions[p] += velocities[p]
energy = 0
for p in range(n_planets):
    energy += sum(abs(positions[p])) * sum(abs(velocities[p]))
print('Energy: {}'.format(energy))

positions = copy.deepcopy(positions_original)
velocities = copy.deepcopy(velocities_original)

lcm = 1
for c in range(3):
    n_iter = 0
    pc = numpy.array([p[c] for p in positions], int)
    vc = numpy.zeros(n_planets, int)
    pco = copy.deepcopy(pc)
    vco = copy.deepcopy(vc)

    while True:
        for pair in itertools.combinations(range(n_planets), 2):
            d = bool(pc[pair[0]] < pc[pair[1]]) - \
                bool(pc[pair[1]] < pc[pair[0]])
            vc[pair[0]] += d
            vc[pair[1]] -= d
        pc += vc
        n_iter += 1
        if (pc == pco).all() and (vc == vco).all():
            lcm = numpy.lcm(lcm, n_iter)
            break
print('Iterations until cycling: {}'.format(lcm))

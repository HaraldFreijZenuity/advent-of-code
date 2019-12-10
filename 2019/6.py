orbits = {}
with open("input/6_map.txt", 'r') as map_txt:
    for line in map_txt.read().splitlines():
        entry = line.split(')')
        orbits[entry[1]] = entry[0]
n_orbits = 0
layer = {}
for obj in orbits:
    layer[obj] = 0
    it_obj = obj
    while it_obj != 'COM':
        layer[obj] += 1
        it_obj = orbits[it_obj]
    n_orbits += layer[obj]
print(n_orbits)
n_steps = 0
c1 = orbits['YOU']
l1 = layer['YOU']
c2 = orbits['SAN']
l2 = layer['SAN']
while(c1 != c2):
    n_steps += 1
    if(l1 > l2):
        c1 = orbits[c1]
        l1 -= 1
    else:
        c2 = orbits[c2]
        l2 -= 1
print(n_steps)

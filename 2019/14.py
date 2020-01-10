import os
import itertools
import numpy


input_file_name = os.path.normpath(os.path.join(os.path.abspath(__file__), '../input/14_reactions.txt'))
reactions = {}
with open(input_file_name, 'r') as reations_file:
    for reaction in reations_file:
        product = reaction.split('=>')[1]
        ingredients = reaction.split('=>')[0].split(',')
        reactions[product.split()[1]] = {'quantity': int(product.split()[0]), 'ingredients': [
            {'name': i.split()[1], 'quantity':int(i.split()[0])} for i in ingredients]}


def update_needs(element, needs):
    r = int(numpy.ceil(needs[element]/reactions[element]['quantity']))
    needs[element] -= r*reactions[element]['quantity']
    assert(needs[element] <= 0)
    for i in reactions[element]['ingredients']:
        needs[i['name']] += r*i['quantity']
        if needs[i['name']] > 0 and i['name'] != 'ORE':
            update_needs(i['name'], needs)


elements = reactions.keys()


def produce(n):
    needs = {}
    for element in elements:
        needs[element] = 0
    needs['FUEL'] = n
    needs['ORE'] = 0
    update_needs('FUEL', needs)
    return needs['ORE']


print("Managed to produce 1 fuel using {} ore".format(produce(1)))

possible = 1
impossible = 1000000000000
while impossible-possible > 1:
    n = int((impossible+possible)/2)
    if produce(n) <= 1000000000000:
        possible = n
    else:
        impossible = n
print("Largest possible prduction: {}".format(possible))

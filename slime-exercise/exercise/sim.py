"""
This module is a story about you and a box of slimes.

01219114 Computer Programming
Week 9, Long Program Assignment: Slime Box (simulation module)
(C) 2022 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

import sys
from slimebox import Slime, Color

# DO NOT MODIFY ABOVE THIS LINE

# Implement this any way you wish.
# You may use objective or procedural methods here.

# Note that the script will start running from the main function.

# Write additional functions here if you need them.

def format_color(c: Color) -> str:
    return f"{c.r} {c.g} {c.b}"

def main(filename):

    # INPUT ZONE (DO NOT MODIFY)

    with open(filename) as input_file:

        s, n = [int(c) for c in input_file.readline().split()]

        slime_lines = []
        order_lines = []

        for i in range(s):
            slime_lines.append(input_file.readline())

        for i in range(n):
            order_lines.append(input_file.readline())

    # END INPUT ZONE

    slimes = []

    for line in slime_lines:
        m, v, r, g, b = [int(c) for c in line.split()]
        slimes.append(Slime(m, v, Color(r, g, b)))

    for line in order_lines:
        values = line.split()
        op = values[0]
        index = int(values[1])
        if op == 'EAT':
            mass = int(values[2])
            foodtype = values[3]
            slimes[index].eat(mass, foodtype)
        elif op == 'SPLIT':
            copies = int(values[2])
            slime = slimes[index]
            slimes[index] = None
            slimes += slime.split(copies)
        elif op == 'COMBINE':
            index2 = int(values[2])
            slimes[index] = slimes[index] + slimes[index2]

    for (index, slime) in enumerate(slimes):
        if slime is not None:
            print(index, slime.mass, slime.volume, format_color(slime.color))

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)

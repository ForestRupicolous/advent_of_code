#! python3
# aoc_02.py
# Advent of code:
# https://adventofcode.com/2021/day/2
# https://adventofcode.com/2021/day/2#part2


# read in sub commands
# pretty (like calculator)
# easy like brute force parsing
# switch case?
# sub class


def pilot_sub(input):
    horz_pos = 0
    depth = 0
    with open(input, 'r') as subctrl:
        ctrl_list = subctrl.readlines()
        print(ctrl_list)
        for ctrl in ctrl_list:
            cmd,value = ctrl.split()
            value = int(value)
            if cmd == 'forward':
                horz_pos += value
            elif cmd == 'down':
                depth += value
            elif cmd == 'up':
                depth -= value
            #print(horz_pos, depth, horz_pos*depth)
            

    return horz_pos*depth


print(pilot_sub('aoc_02_example.txt'))
print(pilot_sub('aoc_02_input.txt'))
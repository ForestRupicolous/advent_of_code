from collections import defaultdict

def day23_part1(input):
    a, b = 0, 0
    with open(input, 'r') as subctrl:
        cmd_list = subctrl.readlines()
        pdr_cmd = [cmd.split() for cmd in cmd_list]
    print(cmd_list)
    print(pdr_cmd)
    return 0


print("Part 1: ", day23_part1('2015_day_23.inp.txt'))
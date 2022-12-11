#! python3
# 2022_aoc_10.py
# Advent of code:
# https://adventofcode.com/2022/day/1
# https://adventofcode.com/2022/day/1#part2
#
def check_cycle(cycle, cur_cycle, reg_x):
    end = False
    res = 0
    list_cycles = [20, 60, 100, 140, 180, 220]
    if cycle >= list_cycles[cur_cycle]-2:
        print('Cycle:',cycle, list_cycles[cur_cycle], reg_x, list_cycles[cur_cycle]* reg_x, cur_cycle)
        res = list_cycles[cur_cycle] * reg_x
        cur_cycle +=1
    if cur_cycle == len(list_cycles):
        end = True
    return res, cur_cycle, end

def check_pxl(cycle, reg_x):
    c = cycle % 40
    if (c >= reg_x -1) and (c <= reg_x +1):
        return '#'
    else:
        return '.'

def part_one(input) -> int:
    with open(input, 'r') as f:
        cycle = 0
        cur_cycle = 0
        reg_x = 1        
        res = 0
        end = False
        data = [line for line in f.readlines()]
        for cmd in data:
            c = cmd.split()[0]
            if c == 'addx':
                r, cur_cycle, end = check_cycle(cycle, cur_cycle, reg_x)
                res += r
                cycle += 2                
                reg_x += int(cmd.split()[1])
            else:
                cycle += 1                
            if end:
                break
    return res

def part_two(input) -> int:
    with open(input, 'r') as f:
        cycle = 0
        reg_x = 1        
        screen = []

        end = False
        data = [line for line in f.readlines()]
        for cmd in data:
            c = cmd.split()[0]
            if c == 'addx':
                for i in range(2):
                    screen.append(check_pxl(cycle, reg_x))
                    cycle += 1              
                reg_x += int(cmd.split()[1])
            else:
                screen.append(check_pxl(cycle, reg_x))
                cycle += 1
        print(len(screen)) 
        print([''.join(screen[x:x+40]) for x in range(0,250,40)])
  
    return 0

if __name__ == "__main__":
    example_path = "./aoc_10_example.txt"
    input_path = "./aoc_10_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(example_path))
    print(part_two(input_path))
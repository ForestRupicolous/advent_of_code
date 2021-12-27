#! python3
# aoc_25.py
# Advent of code:
# https://adventofcode.com/2021/day/25
# https://adventofcode.com/2021/day/25#part2
#
from copy import deepcopy

def part_one(input) -> int:
    with open(input, 'r') as f:
        data = [[x for x in line.strip()] for line in f.readlines()]
        new_data = deepcopy(data)
        #print(data)
        rounds = 0
        has_moved = 1
        NC = len(data[0])
        NR = len(data)
        #print(id(data[0]),id(new_data[0]))
        while has_moved:
        # how to fullfill the only move when it was free before rule and avoid moving it twice?
            has_moved = 0
            for r in range(NR):
                for c in range(NC-1):
                    if data[r][c] == '>' and data[r][c+1] =='.':
                        new_data[r][c] = '.'
                        new_data[r][c+1] = '>'
                        has_moved = 1
                if data[r][NC-1] == '>' and data[r][0] =='.':
                    new_data[r][NC-1] = '.'
                    new_data[r][0] = '>'
                    has_moved = 1
            #print(*(' '.join(row) for row in data), sep='\n')
            #print('------------------------------------')
            data = deepcopy(new_data)
            #print(*(' '.join(row) for row in data), sep='\n')
            #print('################################################################')
            for c in range(NC):
                for r in range(NR-1):
                    if data[r][c] == 'v' and data[r+1][c] =='.':
                        new_data[r][c] = '.'
                        new_data[r+1][c] = 'v'
                        has_moved = 1
                if data[NR-1][c] == 'v' and data[0][c] =='.':
                    new_data[NR-1][c] = '.'
                    new_data[0][c] = 'v'
                    has_moved = 1
            data = deepcopy(new_data)

            rounds += 1
        print('####')
        print(data)


    return rounds

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0

if __name__ == "__main__":
    example_path = "./aoc_25_example.txt"
    input_path = "./aoc_25_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
   # print(part_two(input_path))
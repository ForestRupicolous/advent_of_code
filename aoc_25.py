#! python3
# aoc_25.py
# Advent of code:
# https://adventofcode.com/2021/day/7
# https://adventofcode.com/2021/day/7#part2
#
def part_one(input) -> int:
    with open(input, 'r') as f:
        data = [[x for x in line.strip()] for line in f.readlines()]
        print(data)
        rounds = 0
        has_moved = 1
        NC = len(data[0])
        NR = len(data)

        while has_moved:
        # how to fullfill the only move when it was free before rule and avoid moving it twice?
            has_moved = 0
            for r in range(NR-1,-1,-1):
                for c in range(NC-2,-1,-1):
                    if data[r][c] == '>' and data[r][c+1] =='.':
                        data[r][c] = '.'
                        data[r][c+1] = '>'
                        has_moved = 1
                if data[r][NC-1] == '>' and data[r][0] =='.':
                    data[r][NC-1] = '.'
                    data[r][0] = '>'
                    has_moved = 1
            for c in range(NC-1,-1,-1):
                for r in range(NR-2,0-1,-1):
                    if data[r][c] == 'v' and data[r+1][c] =='.':
                        data[r][c] = '.'
                        data[r+1][c] = 'v'
                        has_moved = 1
                if data[NR-1][c] == 'v' and data[0][c] =='.':
                    data[NR-1][c] = '.'
                    data[0][c] = 'v'
                    has_moved = 1


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
   # print(part_one(input_path))

    print("---Part Two---")
   # print(part_two(input_path))
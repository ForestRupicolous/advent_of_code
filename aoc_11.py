#! python3
# aoc_11.py
# Advent of code:
# https://adventofcode.com/2021/day/11
# https://adventofcode.com/2021/day/11#part2
#
def part_one(input) -> int:
    with open(input, 'r') as inp:
        rows = [digit for line in inp.readlines() for digit in line.strip()]

        #delta colum and delta row
        #up, upright,right,downright, down,downleft,left,upleft
        dr = [-1,-1,0,1,1,1,0,-1]
        dc = [0,1,1,1,0,-1,-1,-1]



        #rows = inp.readlines()
        print(rows)
        print(rows[9][9])

   # elf.board = [[0 for i in range(c)] for j in range(r)]
    return 0

def part_two(input) -> int:
    return 0

if __name__ == "__main__":
    example_path = "./aoc_11_example.txt"
   # input_path = "./aoc_xx_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
   # print(part_one(input_path))

    print("---Part Two---")
   # print(part_two(input_path))
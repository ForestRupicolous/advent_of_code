#! python3
# aoc_20.py
# Advent of code:
# https://adventofcode.com/2021/day/20
# https://adventofcode.com/2021/day/20#part2
#
from aoc_19 import visualize


def part_one(input) -> int:
    with open(input, 'r') as f:
        lines = f.readlines()
        algo = lines[0].strip()
        data = [[int(x) for x in line.strip()] for line in lines[2:]]

        NR = len(data)
        NC = len(data[0])
        pic = [[0 for i in range(-3*NR,5*NR)] for j in range(-3*NC,5*NC)]  
        for step in range(2):
            for r in range(-3*NR,3*NR):
                for c in range(-3*NC,3*NC):
                    val = ''
                    for dr in range(-1,2):
                        for dc in range(-1,2):
                            if 0 <= r+dr < NR and 0 <= c+dc < NC:
                                if step == 0:
                                    val += str(data[r+dr][c+dc])
                                else:
                                    val += str(pic[2*NR+r+dr][2*NC+c+dc])
                            else:
                                val += '0'

                    pic[2*NR+r][2*NC+c]=algo[int(val,2)]

    return sum([r.count('1') for r in pic])

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0

if __name__ == "__main__":
    example_path = "./aoc_20_example.txt"
  #  input_path = "./aoc_20_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
  #  print(part_one(input_path))

    print("---Part Two---")
  #  print(part_two(input_path))
#! python3
# aoc_19.py
# Advent of code:
# https://adventofcode.com/2021/day/19
# https://adventofcode.com/2021/day/19#part2
import numpy as np
#
def part_one(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip().split(',')] for line in f.readlines()]
        vectors = np.array(data)
        print(data)
        print(vectors)
        print(vectors[0])
        for vector in vectors:
            print(vector/np.linalg.norm(vector))
    return 0

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0

if __name__ == "__main__":
    mnml = "./aoc_19_mnml.txt"
    example_path = "./aoc_19_example.txt"
    input_path = "./aoc_19_input.txt"   
    print("---Part One---")
    print(part_one(mnml))
  #  print(part_one(example_path))
 #   print(part_one(input_path))

    print("---Part Two---")
  #  print(part_two(input_path))
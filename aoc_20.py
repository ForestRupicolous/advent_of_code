#! python3
# aoc_20.py
# Advent of code:
# https://adventofcode.com/2021/day/20
# https://adventofcode.com/2021/day/20#part2
#
def part_one(input) -> int:
    with open(input, 'r') as f:
        lines = f.readlines()
        algo = lines[0].strip()
        data = [[int(x) for x in line.strip()] for line in lines[2:]]
        print(algo)
        print(algo[0], algo[-1])
        print(data)
    return 0

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
#! python3
# aoc_07.py
# Advent of code:
# https://adventofcode.com/2021/day/7
# https://adventofcode.com/2021/day/7#part2
#
def part_one(input) -> int:
    with open(input, 'r') as digits:
        in_dig = [line.split('|') for line in digits.readlines()]
        

    print(in_dig)
    return 0

def part_two(input) -> int:
    return 0

if __name__ == "__main__":
    example_path = "./aoc_08_exp.txt"
 #   input_path = "./aoc_xx_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
 #   print(part_one(input_path))

    print("---Part Two---")
  #  print(part_two(input_path))
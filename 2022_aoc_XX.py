#! python3
# 2022_aoc_XX.py
# Advent of code:
# https://adventofcode.com/2022/day/XX
# https://adventofcode.com/2022/day/XX#part2
#
def part_one(input) -> int:
    with open(input, 'r') as f:
        data = [ line.strip() for line in f.readlines()]
    return 0

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0

if __name__ == "__main__":
    example_path = "./aoc_XX_example.txt"
    input_path = "./aoc_XX_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
    #print(part_two(example_path))
    #print(part_two(input_path))
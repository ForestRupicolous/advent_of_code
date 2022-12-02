#! python3
# aoc_02.py
# Advent of code:
# https://adventofcode.com/2022/day/2
# https://adventofcode.com/2022/day/2#part2
#
# %%

rps_trsn = dict('A X':0,'A Y':0,'A Z':0,'B X':0,'B Y':0,'B Z':0, 'C X':0, 'C Y':0, 'C Z':0)
# %%
def part_one(input = "./aoc_02_example.txt") -> int:
    print("hello world")
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]   
    return 0

# %%
def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0


# %%
if __name__ == "__main__":
    example_path = "./aoc_02_example.txt"
    input_path = "./aoc_02_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    #print("---Part Two---")
    #print(part_two(input_path))



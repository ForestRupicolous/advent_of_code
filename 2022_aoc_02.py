#! python3
# aoc_02.py
# Advent of code:
# https://adventofcode.com/2022/day/2
# https://adventofcode.com/2022/day/2#part2
#
# %%
#X Rock 1
#Y Paper 2
#Z Scissor 3
#
rps_trsn_part1 = {'A X':4,'A Y':8,'A Z':3,'B X':1,'B Y':5,'B Z':9, 'C X':7, 'C Y':2, 'C Z':6}
rps_trsn_part2 = {'A X':3,'A Y':4,'A Z':8,'B X':1,'B Y':5,'B Z':9, 'C X':2, 'C Y':6, 'C Z':7}
# %%
def part_one(input = "./aoc_02_example.txt") -> int:
    data = 0
    with open(input, 'r') as f:
        for line in f.readlines():
            data += rps_trsn_part1[line.strip()]
   
    return data

# %%
def part_two(input) -> int:
    data = 0
    with open(input, 'r') as f:
        for line in f.readlines():
            data += rps_trsn_part2[line.strip()]
    
    return data

# %%
if __name__ == "__main__":

    example_path = "./aoc_02_example.txt"
    input_path = "./aoc_02_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(example_path))
    print(part_two(input_path))

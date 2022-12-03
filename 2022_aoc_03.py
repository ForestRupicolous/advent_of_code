#! python3
# 2022_aoc_03.py
# Advent of code:
# https://adventofcode.com/2022/day/3
# https://adventofcode.com/2022/day/3#part2
#
def part_one(input) -> int:
    res = 0
    with open(input, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        for pack in data:
            left_comp = pack[:len(pack)//2:]
            right_comp = pack[len(pack)//2::]
            assert len(right_comp) == len(left_comp)
            for char in left_comp:
                if char in right_comp:
                    res += get_value(char)                
                    break
    return res

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0

def get_value(char):
    if char.isupper():
        return ord(char)-38
    else:
        return ord(char)-96

if __name__ == "__main__":
    example_path = "./aoc_03_example.txt"
    input_path = "./aoc_03_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
    #print(part_one(example_path))
    #print(part_two(input_path))
#! python3
# 2022_aoc_06.py
# Advent of code:
# https://adventofcode.com/2022/day/6
# https://adventofcode.com/2022/day/6#part2
#
def part_one(input) -> int:
    ret = 0
    with open(input, 'r') as f:
        data = f.readlines()[0]
        for i in range(len(data)):
            if len(set(data[i:i+4])) == 4:
                ret = i+4
                break
    return ret

def part_two(input) -> int:
    ret = 0
    with open(input, 'r') as f:
        data = f.readlines()[0]
        for i in range(len(data)):
            if len(set(data[i:i+14])) == 14:
                ret = i+14
                break
    return ret

if __name__ == "__main__":
    example_path = "./aoc_06_example.txt"
    input_path = "./aoc_06_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(example_path))
    print(part_two(input_path))
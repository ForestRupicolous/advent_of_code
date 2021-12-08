#! python3
# aoc_07.py
# Advent of code:
# https://adventofcode.com/2021/day/7
# https://adventofcode.com/2021/day/7#part2
#
def part_one(input) -> int:
    cntr = 0
    with open(input, 'r') as digits:
        lines = digits.readlines()
        in_dig = [line.split('|')[0] for line in lines]
        print("In: ",in_dig)
        out_dig = [line.split('|')[1] for line in lines]
        print("Out:", out_dig)
        out_split = [x.split() for x in out_dig]
        print("Out_split:", out_split)
        for example in out_split:
            for digit in example:
                dig_len = len(digit)
                if dig_len == 2 or dig_len == 3 or dig_len == 4 or dig_len == 7:
                    cntr += 1

    return cntr

def part_two(input) -> int:
    return 0

if __name__ == "__main__":
    example_path = "./aoc_08_exp.txt"
    input_path = "./aoc_08_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
  #  print(part_two(input_path))
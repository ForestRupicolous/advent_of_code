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


#find segments or chars
#chars:
# 1:len()
# 2: f not in string
# 



def part_two(input) -> int:
    cntr = 0
    str_to_digit = dict() # sort chars befor using as key
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


def find_digit_by_length(dlen):
    if dlen == 2:
        return 1
    if dlen == 3:
        return 7
    if dlen == 4:
        return 4
    if dlen == 7:
        return 8
    return False

def find_segment_by_number(slen):
    switch={
        4:'e'
        6:'b'
        9:'f'
        #7 could be g or d
        #8 could be a or c - 
    }
    return switch.get(slen, False)


if __name__ == "__main__":
    example_path = "./aoc_08_exp.txt"
    input_path = "./aoc_08_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
  #  print(part_two(input_path))
#! python3
# 2022_aoc_05.py
# Advent of code:
# https://adventofcode.com/2022/day/5
# https://adventofcode.com/2022/day/5#part2
#
import re

def part_one(input) -> int:
    with open(input, 'r') as f:
        regx = re.compile(r"move (\d*) from (\d*) to (\d*)")
        data = [line for line in f.readlines()]
        #ship = ["ZN","MCD","P"]
        ship = ["CFBLDPZS","BWHPGVN","GJBWF","SCWLFNJG","HSMPTLJW","SFGWCB","WBQMPTH","TWSF","RCN"]
        ship = [x[::-1] for x in ship]
        for line in data :
            m = regx.match(line)
            if m:
                cnt = int(m.group(1))
                move = ship[int(m.group(2))-1][-cnt:]
                ship[int(m.group(2))-1]=ship[int(m.group(2))-1][:-cnt]
                ship[int(m.group(3))-1]+=move[::-1]
    return ''.join([x[-1] for x in ship])

def part_two(input) -> int:
    with open(input, 'r') as f:
        regx = re.compile(r"move (\d*) from (\d*) to (\d*)")
        data = [line for line in f.readlines()]
        #ship = ["ZN","MCD","P"]
        ship = ["CFBLDPZS","BWHPGVN","GJBWF","SCWLFNJG","HSMPTLJW","SFGWCB","WBQMPTH","TWSF","RCN"]
        ship = [x[::-1] for x in ship]
        for line in data :
            m = regx.match(line)
            if m:
                cnt = int(m.group(1))
                move = ship[int(m.group(2))-1][-cnt:]
                ship[int(m.group(2))-1]=ship[int(m.group(2))-1][:-cnt]
                ship[int(m.group(3))-1]+=move[::]
    return ''.join([x[-1] for x in ship])

if __name__ == "__main__":
    example_path = "./aoc_05_example.txt"
    input_path = "./aoc_05_input.txt"   
    print("---Part One---")
   # print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
   # print(part_two(example_path))
    print(part_two(input_path))
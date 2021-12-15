#! python3
# aoc_14.py
# Advent of code:
# https://adventofcode.com/2021/day/14
# https://adventofcode.com/2021/day/14#part2
#
from collections import Counter

def part_one(input,iterations) -> int:
    with open(input, 'r') as f:
        data = [line.strip() for line in f.readlines()]

        rep_dict =dict()
        start = data[0]
        data = data[2:]

        for line in data:
            key,item = line.split(' -> ') 
            rep_dict[key] = key[0]+item+key[1]
        
        for i in range(iterations):
            for key,item in rep_dict.items():
                start = start.replace(key, item)

        
  #  print(data)
 #   print(rep_dict)
    print(start)

    print(Counter(start))
    return 0

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0

if __name__ == "__main__":
    example_path = "./aoc_14_example.txt"
    input_path = "./aoc_14_input.txt"   
    print("---Part One---")
    print(part_one(example_path, 2))
   # print(part_one(input_path, 5))

    print("---Part Two---")
    #print(part_two(input_path))
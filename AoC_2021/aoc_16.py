#! python3
# aoc_16.py
# Advent of code:
# https://adventofcode.com/2021/day/16
# https://adventofcode.com/2021/day/16#part2

from collections import deque

def part_one(input) -> int:
    with open(input, 'r') as f:
        stream = deque()
        data = bin(int(f.readline().strip(),16)) 
        version = int(data[2:5],2)
        id = int(data[5:8],2)
        content = data[8:].strip('0')
        stream = deque(content)
        ints = ''
        while stream.popleft() == '1':
            ints += ''.join([stream.popleft() for b in range(4)])
        ints += ''.join([stream.popleft() for b in range(4)]) #get the last 4
        print(ints)
        print(int(ints,2))    


       # print(data)
       # print(version, id, content, stream)
    return 0

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0

if __name__ == "__main__":
    example_path = "./aoc_16_example.txt"
    input_path = "./aoc_16_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
  #  print(part_one(input_path))

    print("---Part Two---")
  #  print(part_two(input_path))
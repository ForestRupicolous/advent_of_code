#! python3
# aoc_01.py
# Advent of code:
# https://adventofcode.com/2021/day/1
# https://adventofcode.com/2021/day/1#part2

# download input data (optional, for future use)
# Count depth increase (if current num is > last: ++)

# return number of depth increases




def aoc_count_depth_increase(aoc_input):
    prev_depth = 0
    cnt = -1
    with open(aoc_input) as input:
        for depth in input.readlines():
            if int(depth) > prev_depth:
                cnt+=1
            prev_depth = int(depth)
    return cnt

print("Hello World!")
print(aoc_count_depth_increase('aoc_01_example.txt'))
print(aoc_count_depth_increase('aoc_01_input.txt'))


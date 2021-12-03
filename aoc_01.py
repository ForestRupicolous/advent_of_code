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
    with open(aoc_input, 'r') as input:
        for depth in input.readlines():
            if int(depth) > prev_depth:
                cnt+=1
            prev_depth = int(depth)
    return cnt

#2nd challenge - better code as integers are converted in the beginning
def aoc_count_depth_sum_increase(aoc_input, winsize=3):

    prev_depth_sum = 0
    cnt = -1
    with open(aoc_input, 'r') as input:
        depths = list(map(int,input.readlines()))
        print(depths)
        for i in range(len(depths) - winsize + 1):
            window = depths[i: i + winsize]
            depth_sum = sum(window)
            print(window, sum(window))
            if depth_sum > prev_depth_sum:
                cnt+=1
            prev_depth_sum = depth_sum
    return cnt

print("Hello World!")
print(aoc_count_depth_increase('aoc_01_example.txt'))
print(aoc_count_depth_increase('aoc_01_input.txt'))
print(aoc_count_depth_sum_increase('aoc_01_input.txt'))


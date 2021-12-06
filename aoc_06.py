#! python3
# aoc_06.py
# Advent of code:
# https://adventofcode.com/2021/day/6
# https://adventofcode.com/2021/day/6#part2
#
from timeit import default_timer as timer
import math

def fish_sim(fish,days):
    #idea: split into pools of different aged fish
    pool = ([fish.count(i) for i in range(9)])
    for day in range(days):
        pool = pool[1:-2] + [pool[0]+pool[-2]] + [pool[-1]] + [pool[0]]
    return(sum(pool))

    #for day in range(days):
    #    fish = [fish.append(9) or 6 if f == 0 else f-1 for f in fish] # or as append returns none (hack)
    #return (len(fish))

ex_fish = [3,4,3,1,2]
full_fish = [2,5,2,3,5,3,5,5,4,2,1,5,5,5,5,1,2,5,1,1,1,1,1,5,5,1,5,4,3,3,1,2,4,2,4,5,4,5,5,5,4,4,1,3,5,1,2,2,4,2,1,1,2,1,1,4,2,1,2,1,2,1,3,3,3,5,1,1,1,3,4,4,1,3,1,5,5,1,5,3,1,5,2,2,2,2,1,1,1,1,3,3,3,1,4,3,5,3,5,5,1,4,4,2,5,1,5,5,4,5,5,1,5,4,4,1,3,4,1,2,3,2,5,1,3,1,5,5,2,2,2,1,3,3,1,1,1,4,2,5,1,2,4,4,2,5,1,1,3,5,4,2,1,2,5,4,1,5,5,2,4,3,5,2,4,1,4,3,5,5,3,1,5,1,3,5,1,1,1,4,2,4,4,1,1,1,1,1,3,4,5,2,3,4,5,1,4,1,2,3,4,2,1,4,4,2,1,5,3,4,1,1,2,2,1,5,5,2,5,1,4,4,2,1,3,1,5,5,1,4,2,2,1,1,1,5,1,3,4,1,3,3,5,3,5,5,3,1,4,4,1,1,1,3,3,2,3,1,1,1,5,4,2,5,3,5,4,4,5,2,3,2,5,2,1,1,1,2,1,5,3,5,1,4,1,2,1,5,3,5,2,1,3,1,2,4,5,3,4,3]
start = timer()
print(fish_sim(full_fish,256))
end = timer()
print(end - start)



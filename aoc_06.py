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
    # grows only happens every 7 day... all fish that are < mood 7 days
    # directly calc number
    print(days%7)
    pool = list()
    #exp = len(fish)*pow(2,days/7)
    calc_direct = len(fish)*math.exp(days*math.log(days/7))
    pool = [fish.count(i) if (i < days%7) else fish.count(i)-1 if fish.count(i)>0 else 0 for i in range(8)]
    cnt_fish = [age*pow(2,days/9) for age in pool]
    print(pool, cnt_fish, sum(cnt_fish))


    for day in range(days):
        fish = [fish.append(9) or 6 if f == 0 else f-1 for f in fish] # or as append returns none (hack)
        #for i in range(len(fish)):
        #    fish[i]-=1
        #    if fish[i] == -1:
        #        fish[i] = 6
        #        fish.append(8)
        #print("Fish after day", day , fish)
    return len(fish),calc_direct

ex_fish = [7]
#ex_fish = [3,4,3,1,2]
full_fish = [2,5,2,3,5,3,5,5,4,2,1,5,5,5,5,1,2,5,1,1,1,1,1,5,5,1,5,4,3,3,1,2,4,2,4,5,4,5,5,5,4,4,1,3,5,1,2,2,4,2,1,1,2,1,1,4,2,1,2,1,2,1,3,3,3,5,1,1,1,3,4,4,1,3,1,5,5,1,5,3,1,5,2,2,2,2,1,1,1,1,3,3,3,1,4,3,5,3,5,5,1,4,4,2,5,1,5,5,4,5,5,1,5,4,4,1,3,4,1,2,3,2,5,1,3,1,5,5,2,2,2,1,3,3,1,1,1,4,2,5,1,2,4,4,2,5,1,1,3,5,4,2,1,2,5,4,1,5,5,2,4,3,5,2,4,1,4,3,5,5,3,1,5,1,3,5,1,1,1,4,2,4,4,1,1,1,1,1,3,4,5,2,3,4,5,1,4,1,2,3,4,2,1,4,4,2,1,5,3,4,1,1,2,2,1,5,5,2,5,1,4,4,2,1,3,1,5,5,1,4,2,2,1,1,1,5,1,3,4,1,3,3,5,3,5,5,3,1,4,4,1,1,1,3,3,2,3,1,1,1,5,4,2,5,3,5,4,4,5,2,3,2,5,2,1,1,1,2,1,5,3,5,1,4,1,2,1,5,3,5,2,1,3,1,2,4,5,3,4,3]
start = timer()
print(fish_sim(ex_fish,80))
end = timer()
print(end - start)



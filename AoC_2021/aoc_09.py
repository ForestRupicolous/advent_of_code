#! python3
# aoc_09.py
# Advent of code:
# https://adventofcode.com/2021/day/9
# https://adventofcode.com/2021/day/9#part2
#
def part_one(input) -> int:
    d = list()
    lowpoints = dict ()
    risk = 0

    i = 1
    j = 1
    with open(input, 'r') as digits:

        lines = digits.readlines()
        dmap = [[99 for i in range(102)] for j in range(len(lines)+2)]       
        for line in lines:
            d.append(line.strip())
        dmap = [[99 for i in range(len(d[0])+2)] for j in range(len(lines)+2)]  
        for line in d:
            for digit in line:
                dmap[j][i]=int(digit)
                i+=1
            i = 1
            j +=1
        ##
        for i in range(1,len(d[0])+1):
            col_sum = 0
            for l in range(1,len(lines)+1):
                value = dmap[l][i]
                neightbors = (dmap[l-1][i],dmap[l+1][i],dmap[l][i-1],dmap[l][i+1])
                for neightbor in neightbors:
                    if neightbor <= value:
                        break
                else:
                    print("Minimum:", value, "x:",i, "y:",l)
                    risk += value+1

    return risk

def part_two(input) -> int:
    import math
    #idea, for each field increase value of lower neigthbor by own value
    d = list()
    lowpoints = dict ()
    risk = 0

    i = 1
    j = 1
    with open(input, 'r') as digits:
        lines = digits.readlines()
        dmap = [[99 for i in range(102)] for j in range(len(lines)+2)]  
        for line in lines:
            d.append(line.strip())
        dmap = [[99 for x in range(len(d[0])+2)] for y in range(len(lines)+2)]
        basins =  [[1 for x in range(len(d[0])+2)] for y in range(len(lines)+2)]  
        for digitline in d:
            for digit in digitline:
                dmap[j][i]=int(digit)
                i+=1
            i = 1
            j +=1
        for times in range(1000):
            for i in range(1,len(d[0])+1):
                for l in range(1,len(lines)+1):
                    value = dmap[l][i]
                    if value != 9:
                        #shift value in lower direction
                        if dmap[l-1][i] < value:
                            basins[l-1][i] += basins[l][i]
                            basins[l][i] = 0
                        elif dmap[l+1][i] < value:
                            basins[l+1][i] += basins[l][i]
                            basins[l][i] = 0
                        elif dmap[l][i-1] < value:
                            basins[l][i-1] += basins[l][i]
                            basins[l][i] = 0                         
                        elif dmap[l][i+1] < value:
                            basins[l][i+1] += basins[l][i]
                            basins[l][i] = 0
    all_basins = [ item for innerlist in basins for item in innerlist ]                     
    all_basins.sort()
    print(basins)
    basins.sort()
    print(basins)
    print(all_basins)
    print(all_basins[-3:])
    return math.prod(all_basins[-3:])

if __name__ == "__main__":
    example_path = "./aoc_09_example.txt"
    input_path = "./aoc_09_input.txt"   
    print("---Part One---")
  #  print(part_one(example_path))
   # print(part_one(input_path))

    print("---Part Two---")
  #  print(part_two(example_path))
    print(part_two(input_path))
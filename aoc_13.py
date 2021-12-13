#! python3
# aoc_13.py
# Advent of code:
# https://adventofcode.com/2021/day/13
# https://adventofcode.com/2021/day/13#part2
#

def part_one(input) -> int:
    nmap =[]
    ymap = []
    with open(input, 'r') as inp:
        lines = inp.readlines()
        R = 15#len(lines)
        C = 11#len(lines[0])
        dmap = [[0 for columns in range(C)] for rows in range(R)]
        
        print(dmap)
        #x-fold
        x = 6
        for row in dmap:
            nmap.append([x + y for x, y in zip(row[:x-1], row[x:])])
            print(nmap)

        #y-fold
        yfold = 7
        for y in range(yfold):
            ymap.append([x + y for x, y in zip(dmap[y][:], dmap[-y][:])])
    print(ymap)


    return 0

def yfold(map,yf):
    nmap = []
    for y in range(yf):
        nmap.append([x + y for x, y in zip(map[y][:], map[-y][:])])
    return nmap

def xfold(map,xf):
    nmap =[]
    for row in map:
        nmap.append([x + y for x, y in zip(row[:xf-1], row[xf:])])
    return nmap


def part_two(input) -> int:
    return 0

if __name__ == "__main__":
   # ex_folds = 
  #  inp_folds = 
    example_path = "./aoc_13_example.txt"
    input_path = "./aoc_13_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
 #   print(part_one(input_path))

    print("---Part Two---")
 #   print(part_two(input_path))
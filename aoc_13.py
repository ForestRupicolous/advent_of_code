#! python3
# aoc_13.py
# Advent of code:
# https://adventofcode.com/2021/day/13
# https://adventofcode.com/2021/day/13#part2
#

def part_one(input) -> int:
    nmap =[]
    ymap = []
    coords = []
    with open(input, 'r') as inp:
        lines = inp.readlines()

        for line in lines:
            line.strip()
            coords.append([int(line.split(',')[1]),int(line.split(',')[0])])

        R = 447*2+1 #max([_[0] for _ in coords])+1
        C = 655*2+1 #max([_[1] for _ in coords])+1
        print('R:',R,'C:',C)
        dmap = [[0 for columns in range(C)] for rows in range(R)]
        for l in coords:
            dmap[l[0]][l[1]] = 1

        dmap = xfold(dmap,655)
        dmap = yfold(dmap,447)  
        dmap = xfold(dmap,327)  
        dmap = yfold(dmap,223)  
        dmap = xfold(dmap,163)  
        dmap = yfold(dmap,111)  
        dmap = xfold(dmap,81)  
        dmap = yfold(dmap,55)  
        dmap = xfold(dmap,40)  
        dmap = yfold(dmap,27)  
        dmap = yfold(dmap,13)  
        dmap = yfold(dmap,6)   

    for line in dmap:
        print(line)

    return sum([sum(i) for i in dmap])

def yfold(m,yf):
    nmap = []
    for y in range(yf):
        nmap.append([x or y for x, y in zip(m[:][y], m[:][-y-1])])
    return nmap

def xfold(m,xf):
    nmap =[]
    for row in m:
        nmap.append([x or y for x, y in zip(row[:xf], row[:xf:-1])])#list reverse [::-1]
    return nmap


def part_two(input) -> int:
    return 0

if __name__ == "__main__":
   # ex_folds = 
  #  inp_folds = 
    example_path = "./aoc_13_example.txt"
    input_path = "./aoc_13_input.txt"   
    print("---Part One---")
 #   print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
 #   print(part_two(input_path))


 
#fold along x=655
#fold along y=447
#fold along x=327
#fold along y=223
#fold along x=163
#fold along y=111
#fold along x=81
#fold along y=55
#fold along x=40
#fold along y=27
#fold along y=13
#fold along y=6
#! python3
# aoc_11.py
# Advent of code:
# https://adventofcode.com/2021/day/11
# https://adventofcode.com/2021/day/11#part2
#
def part_one(input) -> int:
    octo = []
    flashes = 0
    with open(input, 'r') as inp:

        #WHY thsi works and 
        # rows.append([int(x) for line in inp.readlines() for x in list(line.strip())])
        #NOT?
        for line in inp.readlines():
            octo.append([int(x) for x in list(line.strip())])
        #delta colum and delta row
        #up, upright,right,downright, down,downleft,left,upleft
        DR = [-1,-1,0,1,1,1,0,-1]
        DC = [0,1,1,1,0,-1,-1,-1]
        R = len(octo)
        C = len(octo[0])
        flashed = False
        once = True
        for i in range(10):
            for r in range(R):
                for c in range(C):
                    octo[r][c] += 1

            while flashed or once:
                once = False
                for r in range(R):
                    for c in range(C):
                        if octo[r][c] > 9:
                            flashed = True
                            flashes += 1
                            octo[r][c] = 0
                            for d in range(8): #8 directions
                                rr = r+DR[d]
                                cc = c+DC[d]
                                #test for neighbor in  field:
                                if 0 < rr < R and 0 < cc < C:
                                    octo[rr][cc] +=1

        #rows = inp.readlines()
        print(octo)
        print(octo[9][9])

   # elf.board = [[0 for i in range(c)] for j in range(r)]
    return flashes



def part_two(input) -> int:
    return 0

if __name__ == "__main__":
    example_path = "./aoc_11_example.txt"
   # input_path = "./aoc_xx_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
   # print(part_one(input_path))

    print("---Part Two---")
   # print(part_two(input_path))
#! python3
# aoc_11.py
# Advent of code:
# https://adventofcode.com/2021/day/11
# https://adventofcode.com/2021/day/11#part2
#
def part_one(input) -> int:
    rows = []
    octo = []
    flashed = []
    flashes = 0
    with open(input, 'r') as inp:
        #this works
        octo = ([[int(x) for x in line.strip()] for line in inp.readlines()])
        flashed = [[0 for columns in range(10)] for rows in range(10)]
        #NOT?

        #delta colum and delta row
        #up, upright,right,downright, down,downleft,left,upleft
        DR = [-1,-1,0,1,1,1,0,-1]
        DC = [0,1,1,1,0,-1,-1,-1]
        R = len(octo)
        C = len(octo[0])
        flashed = False
        once = True
        for i in range(10000):
            flashed = [[0 for columns in range(10)] for rows in range(10)]
            once = True
            flash = False
            for r in range(R):
                for c in range(C):
                    octo[r][c] += 1

            while flash or once:
                flash = False
                once = False
                for r in range(R):
                    for c in range(C):
                        if octo[r][c] > 9:
                            flash = True
                            flashes += 1
                            octo[r][c] = 0
                            flashed[r][c] = 1
                            for d in range(8): #8 directions
                                rr = r+DR[d]
                                cc = c+DC[d]
                                #test for neighbor in  field:
                                if 0 <= rr < R and 0 <= cc < C and flashed[rr][cc] == 0:
                                    octo[rr][cc] +=1
                #print(sum(sum(x) for x in flashed))
                if sum(sum(x) for x in flashed) == 100:
                    print("Part 2: synced after",i)
                    return i+1

    return flashes



def part_two(input) -> int:
    return 0

if __name__ == "__main__":
    example_path = "./aoc_11_example.txt"
    input_path = "./aoc_11_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
   # print(part_two(input_path))
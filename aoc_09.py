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

#    print(d)
 #   print(dmap)


    return risk

def part_two(input) -> int:
    return 0

if __name__ == "__main__":
    example_path = "./aoc_09_example.txt"
    input_path = "./aoc_09_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
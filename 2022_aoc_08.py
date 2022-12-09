#! python3
# 2022_aoc_08.py
# Advent of code:
# https://adventofcode.com/2022/day/8
# https://adventofcode.com/2022/day/8#part2
#
def is_visible(data,c,r):
    tree = data[c][r]
    #if all on one side are smaller than its visible
    left = data[c][:r]
    right = data[c][r+1:]
    if all((x < tree for x in left)):
        print("Tree",c,r," is visible from left")
        return True
    if all((x < tree for x in right)):
        print("Tree",c,r," is visible from right")
        return True
    if all(x < tree for i in range(r) for x in data[i][c]):
        print("Tree",c,r," is visible from above")
        return True
    if all(x < tree for i in range(r+1,len(data[c])) for x in data[i][c]):
        print("Tree",c,r," is visible from below")
        return True
    print("Tree",c,r," is invisible")
    return False

def part_one(input) -> int:
    with open(input, 'r') as f:
        cnt_visible = 0
        data = [line.strip() for line in f.readlines()]
        cols = len(data)
        rows = len(data[0])
        cnt_visible = 2*cols + 2* rows - 4
        print(data, cols, rows)
        for c in range(1,cols-1):
            for r in range(1,rows-1):
                if is_visible(data,c,r):
                    cnt_visible +=1

    return cnt_visible

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0

if __name__ == "__main__":
    example_path = "./aoc_08_example.txt"
    input_path = "./aoc_08_input.txt"   
    print("---Part One---")
  #  print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
 #   print(part_two(example_path))
 #   print(part_two(input_path))
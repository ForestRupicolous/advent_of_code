#! python3
# aoc_01.py
# Advent of code:
# https://adventofcode.com/2022/day/1
# https://adventofcode.com/2022/day/1#part2
#
def part_one(input) -> int:
    with open(input, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        elves = sum_supplies(data)                
    print(elves.index(max(elves))+1)      
    return max(elves)

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        elves = sum_supplies(data)
        elves.sort()
    return sum(elves[-3::])


def sum_supplies(data):
    elves = []

    sum_cal =0
    for food in data:
        if not food:
            elves.append(sum_cal)
            sum_cal=0
        else:
            sum_cal+=int(food)
        
    elves.append(sum_cal)
    return elves

if __name__ == "__main__":
    example_path = "./aoc_01_example.txt"
    input_path = "./aoc_01_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))



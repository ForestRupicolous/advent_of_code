#! python3
# 2022_aoc_04.py
# Advent of code:
# https://adventofcode.com/2022/day/1
# https://adventofcode.com/2022/day/1#part2
#
def part_one(input) -> int:
    with open(input, 'r') as f:
        res = 0
        data = [line.strip() for line in f.readlines()]
        for line in data:
            first, second = line.split(',')
            if first == second:
                res +=1
                continue
            fstart, fend = first.split('-')
            sstart, send = second.split('-')
            if ((int(fstart) >= int(sstart)) and (int(fend) <= int(send))) or ((int(fstart) <= int(sstart)) and (int(fend) >= int(send))):
                res +=1
    return res

def part_two(input) -> int:
    with open(input, 'r') as f:
        res = 0
        data = [line.strip() for line in f.readlines()]
        for line in data:
            first, second = line.split(',')
            if first == second:
                res +=1
                continue
            fstart, fend = first.split('-')
            sstart, send = second.split('-')
            if (int(fstart) >= int(sstart) and int(fstart) <= int(send)) or ((int(fstart) <= int(sstart)) and (int(fend) >= int(sstart))):
                res +=1
                continue
    return res

if __name__ == "__main__":
    example_path = "./aoc_04_example.txt"
    input_path = "./aoc_04_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(example_path))
    print(part_two(input_path))
#! python3
# 2022_aoc_03.py
# Advent of code:
# https://adventofcode.com/2022/day/3
# https://adventofcode.com/2022/day/3#part2
#
def part_one(input) -> int:
    res = 0
    with open(input, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        for pack in data:
            left_comp = pack[:len(pack)//2:]
            right_comp = pack[len(pack)//2::]
            assert len(right_comp) == len(left_comp)
            for char in left_comp:
                if char in right_comp:
                    res += get_value(char)                
                    break
    return res

def part_two(input) -> int:
    res = 0
    with open(input, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        for i in range(0,len(data),3):
            charlist = []
            elvegroup = data[i:i+3:]
            #get all that are same in 1 and 2
            for char in elvegroup[0]:
                if char in elvegroup[1]:
                    charlist.append(char)
            #check 3
            for char in charlist:
                if char in elvegroup[2]:  
                    res += get_value(char)           
                    break

    return res

def get_value(char):
    if char.isupper():
        return ord(char)-38
    else:
        return ord(char)-96

if __name__ == "__main__":
    example_path = "./aoc_03_example.txt"
    input_path = "./aoc_03_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(example_path))
    print(part_two(input_path))
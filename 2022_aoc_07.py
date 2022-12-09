#! python3
# 2022_aoc_07.py
# Advent of code:
# https://adventofcode.com/2022/day/07
# https://adventofcode.com/2022/day/07#part2
#
#idea: create tree, recursive calc size
# each ls is accompanied by a cd folder
import  re

def part_one(input) -> int:
    with open(input, 'r') as f:
        current_folder = '/'
        folder_contents = [current_folder]
        data = [line.strip() for line in f.readlines()]
        for line in data:
            f = re.match(r'\$ cd (\w+)',line) #look for folders
            if f:
                folder_contents.append(f.groups()[0])
                continue

            d = re.match(r'(dir \w+)', line) # look for file sizes
            if d:
                folder_contents.append(d.groups()[0])
                continue

            m = re.match(r'(\d+) (\w+\.*\w*)', line) # look for file sizes
            if m:
                folder_contents.append(int(m.groups()[0]))
                continue
        #replace directories with their content       
  
        print(folder_contents)
        result=['/']
        for e in folder_contents:
            if type(e) == str:
                m = re.match(r'dir (\w+)', e)
                if m:
                    print(folder_contents.index(m.groups()[0]))
                    
            else:
                result.append(e)
    print(result)
        #print(sum(folder_contents['a']))
    return 0

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return 0

if __name__ == "__main__":
    example_path = "./aoc_07_example.txt"
    input_path = "./aoc_07_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
  #  print(part_one(input_path))

    print("---Part Two---")
    print(part_two(example_path))
    print(part_two(input_path))
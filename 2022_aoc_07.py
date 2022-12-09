#! python3
# 2022_aoc_07.py
# Advent of code:
# https://adventofcode.com/2022/day/07
# https://adventofcode.com/2022/day/07#part2
#
#idea: create tree, recursive calc size
# each ls is accompanied by a cd folder
import  re

def get_folder_size(folder_contents, element):
    size = 0
    for i,e in enumerate(folder_contents[element]):
        if type(e) == str:
            s = get_folder_size(folder_contents, element+'/'+e)
            folder_contents[element][i] = s
            size += s
        else:
            size += e
    return size

def part_one(input) -> int:
    with open(input, 'r') as f:
        current_folder = '/'
        ls_active = ''
        content = []
        sizes = dict() #size of each thing
        folder_contents = dict()
        data = [line.strip() for line in f.readlines()]
        for line in data:
            l = re.match(r'\$ ls',line) #look for folders
            if l:
                ls_active = current_folder
                continue

            f = re.match(r'\$ cd (\w+)',line) #look for folders
            if f:
                folder_contents[ls_active] = content
                content = []
                current_folder += '/'+f.groups()[0]
                continue

            u = re.match(r'\$ cd \.\.',line) #look for folders
            if u:
                current_folder = current_folder[:current_folder.rfind('/')]
                continue

            d = re.match(r'dir (\w+)', line) # look for file sizes
            if d:
                content.append(d.groups()[0])
                continue

            m = re.match(r'(\d+) (\w+\.*\w*)', line) # look for file sizes
            if m:
                sizes[m.groups()[1]] = int(m.groups()[0])
                content.append(int(m.groups()[0]))
                continue
        folder_contents[current_folder] = content
        
        print(folder_contents)
        #replace directories with their content
        get_folder_size(folder_contents,'/')
        s = 0
        for k,v in folder_contents.items():
            print(k,sum(v),v)
            if sum(v) <= 100000:
                s+=sum(v)
        print(folder_contents)
    return s

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return 0

if __name__ == "__main__":
    example_path = "./aoc_07_example.txt"
    input_path = "./aoc_07_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
 #   print(part_two(example_path))
  #  print(part_two(input_path))
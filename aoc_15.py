#! python3
# aoc_07.py
# Advent of code:
# https://adventofcode.com/2021/day/7
# https://adventofcode.com/2021/day/7#part2
#
from collections import deque

def part_one(input) -> int:


    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
        print(data)
        #up, right, down, left
        DR = [-1,0,1,0]
        DC = [0,1,0,-1]
        R = len(data)
        C = len(data[0])
        # Idee:
        # Min Weg Länge ist R-1 + C-1
        # Grenze ist MinWeg_länge * 9
        # calc all min ways, check,
        # make longer
        # ...
        # kürzester Umweg kostet 3 -> 3x1 -> 2 ist immer billiger
        # 11111
        # 11511
        # immer den billigeren weg zuerst

        #BFS
        # https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/a-search-in-python
        def get_cell_value(cell):
            return data[cell[0]][cell[1]]

        def get_neighbours(cell):
            #up, right, down, left
            DR = [-1,0,1,0]
            DC = [0,1,0,-1]
            neighbours = []
            for i in range(4):
                rr = cell[0]+DR[i]
                cc = cell[1]+DC[i]
                # check if in grid
                if 0<=rr<R and 0<=cc<C:
                    neighbours.append((rr,cc))
            return neighbours

        start = (0,0)
        goal = (R-1,C-1)
        visted = set()
        queue = deque()

        queue.append(start)
        path_len = {start: 0}

        while queue:
            cell = queue.popleft()
            if cell in visted:
                continue
            if cell == goal:
                return path_len[cell]
            visted.add(cell)
            for neighbour in get_neighbours(cell):
                if neighbour not in path_len:
                    path_len[neighbour] = path_len[cell] + get_cell_value(cell)
                queue.append(neighbour)
            print(queue)

    return -1

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0

if __name__ == "__main__":
    example_path = "./aoc_15_example.txt"
    input_path = "./aoc_15_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    #print(part_one(input_path))

    print("---Part Two---")
    #print(part_two(input_path))
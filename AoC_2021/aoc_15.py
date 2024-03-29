#! python3
# aoc_15.py
# Advent of code:
# https://adventofcode.com/2021/day/15
# https://adventofcode.com/2021/day/15#part2
#
from collections import deque

from heapq import heappush, heappop

class PriorityQueue:
    
    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))
    
    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))
    
    def pop(self):
        priority, value = heappop(self.heap)
        return value
    
    def __len__(self):
        return len(self.heap)


def part_one_and_two(input, tiles) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
        #big map

        #up, right, down, left
        DR = [-1,0,1,0]
        DC = [0,1,0,-1]
        R = len(data)
        C = len(data[0])
        #extend the array in both directions by factor 5 and add value to new array
        # modulo 9 for numbers > 9 to count 1-9 for each cell
        data = [[(data[y][x] + i + l) if (data[y][x] + i + l)<=9 else (data[y][x] + i + l)%9 for l in range(tiles) for x in range(R)] for i in range(tiles) for y in range(C)]

        R = len(data)
        C = len(data[0])
        print(len(data), len(data[0]))

        #A* algo
        # https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/a-search-in-python
        start = (0,0)
        goal = (R-1,C-1)
        print(goal)
        visted = set()
        came_from = dict()
        frontier = PriorityQueue()

        def get_cell_value(cell):
            return data[cell[0]][cell[1]]

        def heuristic(cell):
            return max(abs(goal[0]-cell[0]),abs(goal[1]-cell[1]))

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

        distance = {start: 0}
        frontier.add(start)
        while frontier:
            cell = frontier.pop()
            if cell in visted:
                continue
            if cell == goal:
                return distance[cell]
            visted.add(cell)
            for successor in get_neighbours(cell):
                frontier.add(
                    successor,
                    priority = distance[cell] + 1 + heuristic(successor)
                )
                if successor not in distance or distance[cell] + get_cell_value(successor) < distance[successor]:
                    distance[successor] = distance[cell] + get_cell_value(successor)
                    came_from[successor] = cell

    # goal not found
    return -1

if __name__ == "__main__":
    example_path = "./aoc_15_example.txt"
    input_path = "./aoc_15_input.txt"   
    print("---Part own---")
    print('part 1:', part_one_and_two(input_path, 1))
    print("---Part Two---")
    print('part 2:', part_one_and_two(input_path, 5))
    #part one was increased to part to, use original data for part 1

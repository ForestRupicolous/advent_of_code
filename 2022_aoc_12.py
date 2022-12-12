#! python3
# 2022_aoc_12.py
# Advent of code:
# https://adventofcode.com/2022/day/12
# https://adventofcode.com/2022/day/12#part2
#
#reused code of AOC 2021 day 15, train A* alogrithm by using it here.
#At some time I should learn to code it
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

def part_one(input) -> int:
    with open(input, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        #big map

        #up, right, down, left
        DR = [-1,0,1,0]
        DC = [0,1,0,-1]
        R = len(data)
        C = len(data[0])

        print(len(data), len(data[0]))

        #A* algo
        # https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/a-search-in-python
        for i,line in enumerate(data):
            if 'S' in line:
                start = (i,line.index('S'))
                #set correct value for start
                data[start[0]] = data[start[0]].replace('S','a')
                print(start)
            if 'E' in line:
                goal = (i,line.index('E'))
                data[goal[0]] = data[goal[0]].replace('E','z')
                print(goal)

        visited = set()
        came_from = dict()
        frontier = PriorityQueue()

        def get_cell_value(cell):
            return ord(data[cell[0]][cell[1]])

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
                # check if in grid and if climbable, might be better to invert, to climb down

                if (0<=rr<R) and (0<=cc<C):
                    if(get_cell_value(cell) + 1 >= get_cell_value((rr,cc))):
                        neighbours.append((rr,cc))

            return neighbours

        distance = {start: 0}
        frontier.add(start)
        while frontier:
            cell = frontier.pop()
            if cell in visited:
                continue
            if cell == goal:
                return distance[cell]

            visited.add(cell)
            for successor in get_neighbours(cell):
                frontier.add(
                    successor,
                    priority = distance[cell] + 1 + heuristic(successor)
                )
                if successor not in distance or distance[cell] + 1 <= distance[successor]:
                    distance[successor] = distance[cell] + 1
                    came_from[successor] = cell

    # goal not found
    return -1

def part_two(input) -> int:
    #idea: collect all start neightbor 'a's, make a list, make a* from each of them get smallest
    with open(input, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        #big map

        #up, right, down, left
        DR = [-1,0,1,0]
        DC = [0,1,0,-1]
        R = len(data)
        C = len(data[0])

        print(len(data), len(data[0]))

        #A* algo
        # https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/a-search-in-python
        for i,line in enumerate(data):
            if 'S' in line:
                start = (i,line.index('S'))
                #set correct value for start
                data[start[0]] = data[start[0]].replace('S','a')
                print(start)
            if 'E' in line:
                goal = (i,line.index('E'))
                data[goal[0]] = data[goal[0]].replace('E','z')
                print(goal)

        visited = set()
        came_from = dict()
        frontier = PriorityQueue()
        startpoints = PriorityQueue()

        def get_cell_value(cell):
            return ord(data[cell[0]][cell[1]])

        def heuristic(cell):
            return max(abs(goal[0]-cell[0]),abs(goal[1]-cell[1]))

        def get_startingpoints(cell):
            #up, right, down, left
            DR = [-1,0,1,0]
            DC = [0,1,0,-1]
            starts = []
            for i in range(4):
                rr = cell[0]+DR[i]
                cc = cell[1]+DC[i]
                # check if in grid and same starting height
                if (0<=rr<R) and (0<=cc<C):
                    if(get_cell_value(cell) == get_cell_value((rr,cc))):
                        starts.append((rr,cc))
            return starts

        def get_neighbours(cell):
            #up, right, down, left
            DR = [-1,0,1,0]
            DC = [0,1,0,-1]
            neighbours = []
            for i in range(4):
                rr = cell[0]+DR[i]
                cc = cell[1]+DC[i]
                # check if in grid and if climbable, might be better to invert, to climb down

                if (0<=rr<R) and (0<=cc<C):
                    if(get_cell_value(cell) + 1 >= get_cell_value((rr,cc))):
                        neighbours.append((rr,cc))

            return neighbours

        distance = {start: 0}
        startpoints.add(start)

        while startpoints:
            cell = startpoints.pop()
            if cell in visited:
                continue
            if cell == goal:
                return distance[cell]

            visited.add(cell)
            for successor in get_startingpoints(cell):
                startpoints.add(
                    successor,
                    priority = distance[cell] + 1 + heuristic(successor)
                )
                if successor not in distance or distance[cell] + 1 <= distance[successor]:
                    distance[successor] = distance[cell] + 1
                    came_from[successor] = cell
        startpoints = visited

        dists = dict()

        for point in startpoints:
            visited = set()
            came_from = dict()
            frontier = PriorityQueue()
            start = point
            distance = {start: 0}
            frontier.add(start)
            while frontier:
                cell = frontier.pop()

                if cell in visited:
                    continue
                if cell == goal:
                    dists[point] = distance[cell]
                    continue

                visited.add(cell)
                for successor in get_neighbours(cell):
                    frontier.add(
                        successor,
                        priority = distance[cell] + 1 + heuristic(successor)
                    )
                    if successor not in distance or distance[cell] + 1 <= distance[successor]:
                        distance[successor] = distance[cell] + 1
                        came_from[successor] = cell
                        
        print(dists)
    # goal not found
    return min(dists.values())

if __name__ == "__main__":
    example_path = "./aoc_12_example.txt"
    input_path = "./aoc_12_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(example_path))
    print(part_two(input_path))
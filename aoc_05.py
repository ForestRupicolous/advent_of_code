#! python3
# aoc_05.py
# Advent of code:
# https://adventofcode.com/2021/day/5
# https://adventofcode.com/2021/day/5#part2
#


def hello_world():
    return 'hello world'

class ventmap:
    def __init__(self, xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.map = [[0 for i in range(xmax)] for j in range(ymax)]

    

    
def check_line(x1,y1,x2,y2):
    return x1 == x2 or y1 == y2




def find_vents(input):
    mymap = ventmap(1000,1000)
    with open(input, 'r') as line_list:
        for line in line_list.readlines():
            lstart, lend = line.split(' -> ')
            x1,y1 = lstart.split(',')
            x1 = int(x1)
            y1 = int(y1)
            x2,y2 = lend.split(',')
            x2= int(x2)
            y2 = int(y2)
            if check_line(x1,y1,x2,y2):
                if x1>x2 or y1 >y2:
                    x1,x2 = x2,x1
                    y1,y2 = y2,y1
                #print("Line OK:", x1,y1,x2,y2)
                for i in range(x1,x2+1):
                    for l in range(y1,y2+1):
                        mymap.map[l][i]+=1
            #else:
                #print("Line diag:", x1,y1,x2,y2)
    danger_points = 0
    for line in mymap.map:
        for field in line:
            if field > 1:
                danger_points +=1

    return danger_points

print(find_vents("aoc_05_example.txt"))
print(find_vents("aoc_05_input.txt"))
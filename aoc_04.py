#! python3
# aoc_04.py
# Advent of code:
# https://adventofcode.com/2021/day/4
# https://adventofcode.com/2021/day/4#part2

# give the list of nums extra for easier programming


class BBoard:
    def __init__(self, r, c):
        self.board = [[0 for i in range(c)] for j in range(r)]

    def add_row(self,row,i):
        self.board[i][:]=row
        print(self.board)

def play_bingo(input, called_nums ):
    bingoboards = list()
    with open(input, 'r') as boards:
        board_list = boards.readlines()
        print(board_list)
        i = 0
        cur_board = BBoard(5,5)
        for line in board_list:
            row = line.split()
            if len(row)==5:
                cur_board.add_row(row,i)
                i+=1
            if i>4:
                bingoboards.append(cur_board)
                i=0
                cur_board = BBoard(5,5)
                print('########################')       
    return 0

example_nums = (7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1)

print(play_bingo('aoc_04_example.txt', example_nums))
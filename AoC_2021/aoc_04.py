#! python3
# aoc_04.py
# Advent of code:
# https://adventofcode.com/2021/day/4
# https://adventofcode.com/2021/day/4#part2

# give the list of nums extra for easier programming


class BBoard:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.won = False
        self.board = [[0 for i in range(c)] for j in range(r)]

    def add_row(self,row,i):
        self.board[i][:]=list(map(int,row))
        #print(self.board)
    
    def remove_num(self, num):
        for i in range(self.r):
            for l in range(self.c):                
                if self.board[i][l] is num:
                    self.board[i][l] = -1

    def check_rows(self):
        for row in self.board:
            if sum(row) == -5:
                return True
        return False
    
    def check_columns(self):
        for i in range(self.c):
            col_sum = 0
            for l in range(self.r):
                col_sum += self.board[l][i]
                if col_sum == -5:
                    return True
        return False

    def check_board(self):
        self.won = self.check_rows() or self.check_columns()
        return self.won

    def calc_value(self):
        board_sum = 0
        for i in range(self.c):
            for l in range(self.r):
                if self.board[i][l] != -1:
                    board_sum += self.board[i][l]
        return board_sum




def play_bingo(input, called_nums):
    bingoboards = list()
    with open(input, 'r') as boards:
        board_list = boards.readlines()
        print(board_list)
        i = 0
        #create boards
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
        win_count = 0
        for num in called_nums:
            for board in bingoboards:
                board.remove_num(num)
                #print(board.board)
            
            for board in bingoboards:
                if not board.won:
                    if board.check_board():
                        win_count += 1 
                        print("Found:", num)
                        print(board.check_rows())
                        print(board.check_columns())
                        print(bingoboards.index(board))
                        board.calc_value()
                    else:
                        print(bingoboards.index(board))
                        print(board.check_rows())
                        print(board.check_columns())
                        
                if win_count == len(bingoboards):
                    return board.calc_value(), num, board.calc_value() * num
            else:
                print("Not finshed after:", num)
                print(bingoboards[1].board)
    return -1

example_nums = (7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1)
input_nums = (17,58,52,49,72,33,55,73,27,69,88,80,9,7,59,98,63,42,84,37,87,28,97,66,79,77,61,48,83,5,94,26,70,12,51,82,99,45,22,64,10,78,13,18,15,39,8,30,68,65,40,21,6,86,90,29,60,4,38,3,43,93,44,50,41,96,20,62,19,91,23,36,47,92,76,31,67,11,0,56,95,85,35,16,2,14,75,53,1,57,81,46,71,54,24,74,89,32,25,34)
print(play_bingo('aoc_04_example.txt', example_nums))
print(play_bingo('aoc_04_input.txt', input_nums))
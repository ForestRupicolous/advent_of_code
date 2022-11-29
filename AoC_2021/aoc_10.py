#! python3
# aoc_10.py
# Advent of code:
# https://adventofcode.com/2021/day/10
# https://adventofcode.com/2021/day/10#part2
#
def part_one(input) -> int:
    #push / pop with 1 stack,
    char_stack = list()
    opens = ('(','[','{','<')
    closes = (')',']','}','>')
    value = (3,57,1197,25137)
    score = 0
    with open(input, 'r') as inp:
        cmds = [cmd.strip() for cmd in inp.readlines()]
        for line in cmds:
            for char in line:
                if char in opens:
                    char_stack.append(char)
                else:
                    if char != closes[opens.index(char_stack.pop())]:
                        score += value[closes.index(char)]    
            print(char_stack)
    return score

def part_two(input) -> int:
        #push / pop with 1 stack,
    char_stack = list()
    opens = ('(','[','{','<')
    closes = (')',']','}','>')
    value = (1,2,3,4)
    score = 0
    score_list = list()
    
    with open(input, 'r') as inp:
        cmds = [cmd.strip() for cmd in inp.readlines()]

        for line in cmds:
            line_invalid = False
            char_stack.clear()
            for char in line:
                if char in opens:
                    char_stack.append(char)
                else:
                    if char != closes[opens.index(char_stack.pop())]:
                        line_invalid = True
                        break
            
            if not line_invalid:
                print("----",char_stack)
                char_stack.reverse()
                for element in char_stack:
                    score = (score *5) + value[opens.index(element)]
                score_list.append(score)
                score = 0
    score_list.sort()
      
    return score_list[int(len(score_list)/2)]

if __name__ == "__main__":
    example_path = "./aoc_10_example.txt"
    input_path = "./aoc_10_input.txt"   
    print("---Part One---")
  #  print(part_one(example_path))
  #  print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
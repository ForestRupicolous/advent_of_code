#! python3
# aoc_07.py
# Advent of code:
# https://adventofcode.com/2021/day/7
# https://adventofcode.com/2021/day/7#part2
#
def part_one(sp1,sp2) -> int:

    def roll_dice(last_roll):
        return sum([last_roll + i if last_roll+i <=100 else (last_roll+i)%100 for i in range(1,4)])%10

    scores = [0,0]
    pos = [sp1,sp2]
    rolls = 0
    deterdice = 0
    while 1:
        for i in range(len(scores)):
            roll = roll_dice(deterdice)
            deterdice += 3
            if deterdice > 100:
                deterdice -= 100
            newpos = (pos[i] + roll)
            if newpos > 10:
                newpos = newpos % 10
            pos[i] = newpos
            scores[i] += pos[i]
            rolls += 3
            if scores[i]>=1000:
               return min(scores)*rolls, scores, rolls


    return scores

def part_two(sp1,sp2) -> int:
    scores = [0,0]
    univ = [0,0]
    pos = [sp1,sp2]
    while 1:
        for i in range(2):
            scores[i] +=1
            if scores[i] >= 21:
                univ[i] +=1
                break
           

    return univ

if __name__ == "__main__":
   # example_path = "./aoc_xx_example.txt"
   # input_path = "./aoc_xx_input.txt"   
    print("---Part One---")
    print(part_one(7,4))
    #print(part_one(input_path))

    print("---Part Two---")
    print(part_two(4,8)) #expect 444356092776315
    print(part_two(7,4))
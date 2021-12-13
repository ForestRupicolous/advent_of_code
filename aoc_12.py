#! python3
# aoc_12.py
# Advent of code:
# https://adventofcode.com/2021/day/12
# https://adventofcode.com/2021/day/12#part2
# visualisation: https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%0Astart-%3EYY%3B%0Aav-%3Erz%3B%0Arz-%3EVH%3B%0Afh-%3Eav%3B%0Aend-%3Efh%3B%0Ask-%3Egp%3B%0Aae-%3Eav%3B%0AYY-%3Egp%3B%0Aend-%3EVH%3B%0ACF-%3Eqz%3B%0Aqz-%3Eend%3B%0Aqz-%3EVG%3B%0Astart-%3Egp%3B%0AVG-%3Esk%3B%0Arz-%3EYY%3B%0AVH-%3Esk%3B%0Arz-%3Egp%3B%0AVH-%3Eav%3B%0AVH-%3Efh%3B%0Ask-%3Erz%3B%0AYY-%3Esk%3B%0Aav-%3Egp%3B%0Arz-%3Eqz%3B%0AVG-%3Estart%3B%0Ask-%3Efh%3B%0AVG-%3Eav%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D
#
def part_one(input) -> int:
    return 0

def part_two(input) -> int:
    return 0

if __name__ == "__main__":
    example_path = "./aoc_12_example.txt"
    input_path = "./aoc_12_input.txt"   
    print("---Part One---")
    print(part_one(example_path))
   # print(part_one(input_path))

    print("---Part Two---")
   # print(part_two(input_path))
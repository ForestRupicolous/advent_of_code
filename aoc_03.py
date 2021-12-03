#! python3
# aoc_03.py
# Advent of code:
# https://adventofcode.com/2021/day/3
# https://adventofcode.com/2021/day/3#part2

# input: list of 5 bit values
# variables: 
#   gamma rate: binary number of most common bit for each position
#   epsilon rate: binary number of the least common bit for each position -> invert of gamma rate
# result: power rate = dez(gamma rate * epsilon rate)

def get_power_rate(input,bits=5):
    gamma_rate = ''
    epsilon_rate = ''
    with open(input, 'r') as report:
        diag_list = report.readlines()
        for i in range(bits):
            zeros = 0
            ones = 0
            
            for line in diag_list:
                if line[i]=='1':
                    ones+=1
                else:
                    zeros+=1
            gamma_rate+=(str(int(ones > zeros)))
            epsilon_rate+=(str(int(ones < zeros))) #could also be inverted gamma rate
        
    return(int(gamma_rate,2)*int(epsilon_rate,2))

print(get_power_rate('aoc_03_example.txt'))
print(get_power_rate('aoc_03_input.txt',12))
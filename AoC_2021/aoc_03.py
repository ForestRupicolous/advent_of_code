#! python3
# aoc_03.py
# Advent of code:
# https://adventofcode.com/2021/day/3
# https://adventofcode.com/2021/day/3#part2

# input: list of x bit values
# variables: 
#   gamma rate: binary number of most common bit for each position
#   epsilon rate: binary number of the least common bit for each position -> invert of gamma rate
# result: power rate = dez(gamma rate * epsilon rate)

# part 2:
# return: life support rating: oxygen generator rating * CO2 scrubber rating
# variables:
#   oxygen generator rating: 

def get_gamma_epsilon(input,bits=5):
    gamma_rate = ''
    epsilon_rate = ''
    with open(input, 'r') as report:
        return calc_ones_zeros(report.readlines())

def calc_ones_zeros(diag_list, bits = 5):
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(bits):
        zeros = 0
        ones = 0
    
        for line in diag_list:
            if line[i]=='1':
                ones+=1
            else:
                zeros+=1
        gamma_rate+=(str(int(ones >= zeros)))
        epsilon_rate+=(str(int(ones < zeros))) #could also be inverted gamma rate
    return gamma_rate, epsilon_rate

def get_power_rate(input,bits=5):
    gamma_rate, epsilon_rate = get_gamma_epsilon(input,bits)       
    return(int(gamma_rate,2)*int(epsilon_rate,2))

def get_life_support_rating(input,bits=5):
   
    with open(input, 'r') as report:
        diag_list = report.readlines()
        #start with the input list and then only use the lists left
        gamma_rate, epsilon_rate = calc_ones_zeros(diag_list,bits)
        oxy_list = clean_list(diag_list, 0, gamma_rate[0])
        co2_list = clean_list(diag_list, 0, epsilon_rate[0])
        for i in range(1,bits):
            if len(oxy_list) > 1:
                oxy_list = clean_list(oxy_list, i,calc_ones_zeros(oxy_list,bits)[0][i])
            if len(co2_list) > 1:
                co2_list = clean_list(co2_list, i,calc_ones_zeros(co2_list,bits)[1][i])

    return(int(oxy_list[0],2)*int(co2_list[0],2))

def clean_list(diag_list, pos, bit):
    return [line for line in diag_list if line[pos]==bit]

print(get_life_support_rating('aoc_03_example.txt'))
print(get_life_support_rating('aoc_03_input.txt',12))
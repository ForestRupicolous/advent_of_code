#! python3
# aoc_01.py
# Advent of code:
# https://adventofcode.com/2021/day/1

# download input data (optional, for future use)
# Count depth increase (if current num is > last: ++)

# return number of depth increases
import urllib.request




def aoc_count_depth_increase(aoc_input):
    proxies = { "http": "http://127.0.0.1:3128/",
            "https": "http://127.0.0.1:3128/"}
    proxy = urllib.request.ProxyHandler(proxies)
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    with urllib.request.urlopen(aoc_input) as input:
    #input = urllib.request.urlopen(aoc_input)
        print(input)
    return 0

print("Hello World!")
aoc_count_depth_increase('https://adventofcode.com/2021/day/1/input')

 input =
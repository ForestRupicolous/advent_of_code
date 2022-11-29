def day2_part1(input):
    size = 0
    with open(input, 'r') as subctrl:
        pkt_list = subctrl.readlines()
        for pkt in pkt_list:
            this_pkg = pkg_paper_size(*list(map(int,pkt.split('x'))))
            size += sum(this_pkg) + min(this_pkg)/2

    return int(size)

def day2_part2(input):
    size = 0
    with open(input, 'r') as subctrl:
        pkt_list = subctrl.readlines()
        for pkt in pkt_list:
            this_pkg_dim = list(map(int,pkt.split('x')))
            calc_band(*this_pkg_dim)

            size += calc_band(*this_pkg_dim)
            this_pkg_dim.remove(max(this_pkg_dim))
            size += calc_slack(*this_pkg_dim)

    return int(size)

def pkg_paper_size(l,w,h):
    return [2*l*w, 2*w*h, 2*h*l]

def calc_band(l,w,h):
    return l*w*h

def calc_slack(m1,m2):
    return m1+m1+m2+m2

print("Day 2, Example Part 1: ", day2_part1('2015_day02_exp.txt'))
print("Day 2, Part 1: ", day2_part1('2015_day_02_input.txt'))
print("Day 2, Example Part 2: ", day2_part2('2015_day02_exp.txt'))
print("Day 2, Part 2: ", day2_part2('2015_day_02_input.txt'))
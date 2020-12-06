#!/usr/bin/python3

def check_slope(right, down):
    pos_in_row = 0
    hits = 0
    for i in range(0, num_rows, down):
        if inp[i][pos_in_row] == '#':
            hits += 1
        pos_in_row += right
        if pos_in_row > row_length - 1:
            pos_in_row -= row_length
    return hits
    

#inp = open("test_input", "r").readlines()
inp = open("input", "r").readlines()

num_rows = 0
for i in range(len(inp)):
    inp[i] = inp[i][:-1]
    num_rows += 1

row_length = len(inp[0])
slope_one = check_slope(1,1)
slope_two = check_slope(3, 1)
slope_three = check_slope(5,1)
slope_four = check_slope(7,1)
slope_five = check_slope(1,2)

print("Part One: Hit Trees = {}".format(slope_two))
print("Trees hit on: s1 - {}, s2 - {}, s3 - {}, s4 - {}, s5 - {}".format(slope_one, slope_two, slope_three, slope_four, slope_five))
print("Part Two: Hit Tree Product = {}".format(slope_one*slope_two*slope_three*slope_four*slope_five))

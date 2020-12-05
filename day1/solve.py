#!/usr/bin/python3

#inp = open("test_input", "r").readlines()
inp = open("input", "r").readlines()

for i in range(len(inp)):
    inp[i] = int(inp[i][:-1])

done_flag = 0
for line in inp:
    for n_line in inp:
        if (line + n_line) == 2020:
            print("Solved Part One! val1: {}, val2: {}, product: {}".format(line,n_line,line*n_line))
            done_flag = 1
            break
    if done_flag:
        break

done_flag = 0
for line in inp:
    for n_line in inp:
        for m_line in inp:
#            print("{} + {} + {} = {}".format(line, n_line, m_line, line*n_line*m_line))
            if (line + n_line + m_line) == 2020:
                print("Solved Part Two! val1: {}, val2: {}, val3: {}, product: {}".format(line,n_line,m_line,line*n_line*m_line))
                done_flag = 1
                break
        if done_flag:
            break


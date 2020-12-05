#!/usr/bin/python3

inp = open("test_input", "r").readlines()
#inp = open("input", "r").readlines()

for i in range(len(inp)):
    inp[i] = inp[i][:-1]

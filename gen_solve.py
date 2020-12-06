#!/usr/bin/python3

with open("test_input", "r") as f:
#with open("input", "r") as f:
    inp = f.readlines()

for i in range(len(inp)):
    inp[i] = inp[i].rstrip()

print(inp)

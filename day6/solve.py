#!/usr/bin/python3

from collections import Counter

#with open("test_input", "r") as f:
with open("input", "r") as f:
    inp = f.read().split("\n\n")

part1_inp = inp.copy()
for i in range(len(part1_inp)):
    part1_inp[i] = inp[i].replace("\n", "")

#print(inp)

num_yesses = 0

for group in part1_inp:
    uniq = set(group)
#    print(len(uniq))
    num_yesses += len(uniq)
print("Part One: Number of Yesses - {}".format(num_yesses))

num_yesses = 0
for group in inp:
    seen = []
    num_users = 0
    for user in group.rstrip().split("\n"):
        num_users += 1
        for ans in user:
            seen.append(ans)
    c = dict(Counter(seen))
    for val in c:
        if c[val] == num_users:
            num_yesses += 1
print("Part Two: Number of Yesses - {}".format(num_yesses))

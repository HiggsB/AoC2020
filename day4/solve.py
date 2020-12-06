#!/usr/bin/python3

#inp = open("test_input", "r").read().split("\n\n")
inp = open("input", "r").read().split("\n\n")

for i in range(len(inp)):
    inp[i] = inp[i].replace("\n"," ")

valid_passports = 0
for passport in inp:
#    print(passport)
    if "byr" not in passport:
        continue
    if "iyr" not in passport:
        continue
    if "eyr" not in passport:
        continue
    if "hgt" not in passport:
        continue
    if "hcl" not in passport:
        continue
    if "ecl" not in passport:
        continue
    if "pid" not in passport:
        continue
    valid_passports += 1

print("Part One: Valid Passports = {}".format(valid_passports))

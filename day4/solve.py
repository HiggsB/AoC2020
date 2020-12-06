#!/usr/bin/python3

import re

#inp = open("test_input", "r").read().split("\n\n")
inp = open("input", "r").read().split("\n\n")

for i in range(len(inp)):
    inp[i] = inp[i].replace("\n"," ")

valid_passports = 0
for passport in inp:
    if "byr" not in passport:
        continue
    byr = int(passport.split("byr")[1][1:].split(" ")[0])
    if (byr < 1920) or (byr > 2002):
        continue

    if "iyr" not in passport:
        continue
    iyr = int(passport.split("iyr")[1][1:].split(" ")[0])
    if (iyr < 2010) or (iyr > 2020):
        continue

    if "eyr" not in passport:
        continue
    eyr = int(passport.split("eyr")[1][1:].split(" ")[0])
    if (eyr < 2020) or (eyr > 2030):
        continue

    if "hgt" not in passport:
        continue
    hgt = passport.split("hgt")[1][1:].split(" ")[0]
    if not re.search(r'^\d\d*(in|cm)$', hgt):
        continue
    units = hgt[len(hgt)-2:]
    value = int(hgt[:-2])
    if re.search(r'cm', hgt):
        if (value < 150) or (value > 193):
            continue
    if re.search(r'in', hgt):
        if (value < 59) or (value > 76):
            continue

    if "hcl" not in passport:
        continue
    hcl = passport.split("hcl")[1][1:].split(" ")[0]
    if not re.search(r'^#[0-9,a-f]{6}$', hcl):
        continue

    if "ecl" not in passport:
        continue
    ecl = passport.split("ecl")[1][1:].split(" ")[0]
    if not re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', ecl):
        continue

    if "pid" not in passport:
        continue
    pid = passport.split("pid")[1][1:].split(" ")[0]
    if not re.search(r'^\d{9}$', pid):
        continue

    valid_passports += 1

print("Part One: Valid Passports = {}".format(valid_passports))

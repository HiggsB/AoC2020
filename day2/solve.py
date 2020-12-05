#!/usr/bin/python3

#inp = open("test_input", "r").readlines()
inp = open("input", "r").readlines()

for i in range(len(inp)):
    inp[i] = inp[i][:-1]

valid_passwords = 0
for line in inp:
    min_uses = int(line.split('-')[0])
    max_uses = int(line.split('-')[1].split(' ')[0])
#    print("min_uses: {}, max_uses: {}".format(min_uses, max_uses))
    letter = line.split(' ')[1][0]
#    print(letter)
    password = line.split(':')[1][1:]
#    print(password)
    num_occurances = 0
    uses = 0
    for char in password:
        if char == letter:
            uses += 1

    if min_uses <= uses <= max_uses:
        valid_passwords += 1

print("Part One: Valid passwords - {}".format(valid_passwords))

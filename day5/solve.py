#!/usr/bin/python3

#with open("test_input", "r") as f:
with open("input", "r") as f:
    inp = f.readlines()

for i in range(len(inp)):
    inp[i] = inp[i].rstrip()

max_seat_id = 0
possible_seats = list(range(8, 849))
for seat in inp:
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    row = 0
    col = 0
    for char in seat:
        if char == "F":
            if max_row - min_row == 1:
                row = min_row
            else:
                max_row = max_row - round((max_row - min_row)/2)
        elif char == "B":
            if max_row - min_row == 1:
                row = max_row
            else:
                min_row = min_row + round((max_row - min_row)/2)
        elif char == "L":
            if max_col - min_col == 1:
                col = min_col
            else:
                max_col = max_col - round((max_col - min_col)/2)
        elif char == "R":
            if max_col - min_col == 1:
                col = max_col
            else:
                min_col = min_col + round((max_col - min_col)/2)

    seat_id = row * 8 + col
    if seat_id > max_seat_id:
        max_seat_id = seat_id
    possible_seats.remove(seat_id)
#    print("Seat: {}, Row: {}, Col: {}, ID: {}".format(seat, row, col, seat_id))
print("Part One: Max Seat ID - {}".format(max_seat_id))
print(possible_seats)

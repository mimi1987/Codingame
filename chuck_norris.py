import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for c in message:
    binary = format(ord(c), 'b')
    for i, bit in enumerate(binary):
        if int(bit) == 0 and i == 0:
            print("00 0", end="")
        elif int(bit) == 1 and i == 0:
            print("0 0", end="")
        elif int(bit) == 1 and i >= 1 and int(binary[i-1]) == 1:
            print("0", end="")
        elif int(bit) == 0 and int(binary[i-1]) == 1 and i >= 1:
            print(" 00 0", end="")
        elif int(bit) == 0 and int(binary[i-1]) == 0 and i >= 1:
            print("0", end="")
        elif int(bit) == 1 and int(binary[i-1]) == 0 and i >=1:
            print(" 0 0", end="")
    print(end=" ")

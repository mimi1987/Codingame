import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input().upper()

rows = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

for i in range(h):
    rows.append(input())

for row in rows:
    for z in t:
        fi = alphabet.find(z)
        if fi != -1:
            print(row[l*fi:l*(fi+1)], end="")
        else:
            fi = len(alphabet)-1
            print(row[l*fi:l*(fi+1)], end="")
    print()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

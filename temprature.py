import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
pos = []
neg = []


for i in input().split():
    t = int(i)
    if (t == 0 or t > 0):
        pos.append(t)
    else:
        neg.append(t)

pos.sort()
neg.sort(reverse = True)

if (pos == [] and neg == []):
    print(0)
elif 0 in pos:
    print(0)
elif (pos != [] and neg != []):
        if (pos[0] == abs(neg[0])):
            print(pos[0])
        elif (pos[0] < abs(neg[0])):
              print(pos[0])
        else:
              print(neg[0])
elif (neg != [] and pos == []):
    print(neg[0])
elif (neg == [] and pos != []):
    print(pos[0])


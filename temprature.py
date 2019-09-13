import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# 1. sorting the input tempratures into negative and positive values
positive_tempratures = []
negative_tempratures = []

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    
    if t >= 0:
        positive_tempratures.append(t)
    else:
        negative_tempratures.append(t)

# 2. sorting the negative and positive temprature list increasing order
positive_tempratures.sort()
negative_tempratures.sort(reverse=True)

# 3. test for no input values
if not positive_tempratures and not negative_tempratures:
    print("0")

# 4.
#   Test if a zero is in the positive_tempratures list
#   compare the two smallest values if the substract to zero, if so output the first value from the positive temp list
#   compare if they are resulting into a negative number, if so output the first positive temp value
#   compare if they the values resulting into a positive number, if so output the first negative temp value
if 0 in positive_tempratures:
    print("0")
elif positive_tempratures and negative_tempratures:
    if positive_tempratures[0] + negative_tempratures[0] == 0:
        print("{}".format(positive_tempratures[0]))
    elif positive_tempratures[0] + negative_tempratures[0] < 0:
        print("{}".format(positive_tempratures[0]))
    elif positive_tempratures[0] + negative_tempratures[0] > 0:
        print("{}".format(negative_tempratures[0]))
    else:
        print("Don't know yet what went wrong!")
elif not positive_tempratures and negative_tempratures:
    print("{}".format(negative_tempratures[0]))
elif positive_tempratures and not negative_tempratures:
    print("{}".format(positive_tempratues[0]))

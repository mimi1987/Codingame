""" I think there is an error in the chuck norris testcases, there are some spaces missing when a new char is convertet into the
chuck norris code. If I test my code here I can match the binary conversion with my chuck norris code fine with no errors.
So I think the puzzle has some errors. """

message = "Chuck Norris' keyboard has 2 keys: 0 and white space."

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
print()
for char in message:
    print(format(ord(char), 'b'), end="")

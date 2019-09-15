###################################################################
#                   Just works 50 % a the moment                  #
#                                                                 #
#                                                                 #
###################################################################


######################################
# Must be omitted in actual solution
message = "CC"
binary = ""
######################################

for c in message:
    binary += format(ord(c), 'b')

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
    #print(end=" ")

###########################################################
# To see binary representation for debugging purposes only!
# Must be omitted in actual solution
print()
for char in message:
    print(format(ord(char), 'b'), end="")
############################################################
            
        
            

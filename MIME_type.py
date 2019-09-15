import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
mime_types = {}

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_types[ext.lower()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    file_ext = re.search("\.+(\w+)$", fname, flags=re.IGNORECASE)
    if file_ext:
        file_ext = file_ext.group(1).lower()
        if file_ext in mime_types:
            print(mime_types[file_ext])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
    

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

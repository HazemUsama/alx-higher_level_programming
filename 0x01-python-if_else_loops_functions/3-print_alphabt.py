#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i == ord('q') or i == ord('e'):
        continue
    print("{char:c}".format(char=i), end="")

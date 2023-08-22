#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        add = 0
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            add = ord('A') - ord('a')
        print("{}".format(chr(ord(ch) + add)), end="")
    print("")

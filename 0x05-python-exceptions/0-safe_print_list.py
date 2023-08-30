#!/usr/bin/python3
def safe_print_list(args, x):
    num = 0
    for i in range(x):
        try:
            print(args[i], end="")
        except IndexError:
            break
        num += 1
    print("")
    return num

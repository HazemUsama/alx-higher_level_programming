#!/usr/bin/python3
def safe_print_list(args, x):
    for i in range(x):
        try:
            print(args[i], end="")
        except IndexError:
            break
    print("");

#!/usr/bin/python3
def safe_print_list(args, x):
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(args[i]), end="")
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
        num += 1
    print("")
    return num

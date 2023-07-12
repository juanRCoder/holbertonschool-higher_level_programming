#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arguments = len(sys.argv) - 1
    total = 0
    if arguments == 0:
        print("0")
    else:
        for arg in range(1, arguments + 1):
            total += int(sys.argv[arg])
        print("{}".format(total))

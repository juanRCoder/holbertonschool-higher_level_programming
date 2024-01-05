#!/usr/bin/python3
if __name__ == "__main__":
    for i in range(100):
        if i != 99:
            print("{:02d}, ".format(i), end="")
        else:
            print("{}".format(i))

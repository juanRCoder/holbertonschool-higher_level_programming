#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{}".format(value))
    except (ValueError, TypeError) as e:
        print("Exception:", e, file=sys.stderr)
        return False
    else:
        return True

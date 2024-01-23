#!/ust/bin/python3
"""method that contain an function"""


def add_attribute(obj, att, value):
    """ add new attribute if is posible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)

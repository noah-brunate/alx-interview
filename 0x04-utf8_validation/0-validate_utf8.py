#!/usr/bin/python3
"""
script defines a function validUTF8(data) that if agiven
dataset represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Function returns True if data represents
       a valid UTF-8 encoding or False otherwise
    """

    # initialize expected bytes
    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            if (num >> 7) == 0b0:
                continue
            elif (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False

            # num_bytes resets to 0, when all
            # bytes are looped over
            num_bytes -= 1

    # return True if num_bytes is 0 at end of the loop
    return num_bytes == 0

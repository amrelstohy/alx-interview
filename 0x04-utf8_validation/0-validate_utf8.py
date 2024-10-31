#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    A method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    if not isinstance(data, list):
        return False

    data_len = len(data)
    index = 0

    while index < data_len:
        byte = data[index]

        if not isinstance(byte, int):
            return False
        if byte > 255 or byte < 0:
            return False

        bin_byte = format(byte, '08b')

        if bin_byte[0:5] == '11110':
            try:
                if all(
                       format(data[index + i], '08b')[:2] == '10'
                       for i in range(1, 4)
                ):
                    index += 4
                    continue
                else:
                    return False
            except Exception:
                return False

        elif bin_byte[0:4] == '1110':
            try:
                if all(
                    format(data[index + i], '08b')[:2] == '10'
                    for i in range(1, 3)
                ):
                    index += 3
                    continue
                else:
                    return False
            except Exception:
                return False

        elif bin_byte[0:3] == '110':
            try:
                if format(data[index + 1], '08b')[:2] == '10':
                    index += 2
                    continue
                else:
                    return False
            except Exception:
                return False
        elif bin_byte[0:1] == '0':
            index += 1
            continue
        else:
            return False
    return True

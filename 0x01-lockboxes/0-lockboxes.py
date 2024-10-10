#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Lockboxes"""

    if not isinstance(boxes, list):
        return False

    keys = boxes[0]

    if 0 not in boxes:
        keys.append(0)

    for key in keys:
        for k in boxes[key]:
            if k not in keys:
                keys.append(k)

    if len(keys) == len(boxes):
        return True
    else:
        return False

#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Lockboxes"""

    keys = boxes[0]
    num_boxes = len(boxes)

    if 0 not in boxes:
        keys.append(0)

    for key in keys:
        if key > num_boxes - 1:
            keys.remove(key)
            continue

        for k in boxes[key]:
            if k not in keys:
                keys.append(k)

    if len(set(keys)) == num_boxes:
        return True
    else:
        return False

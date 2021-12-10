#!/usr/bin/python3
"""Lock boxes"""


def can_unlock_all(boxes):
    """Check if all of boxes can be opened"""
    if not boxes[0] and len(boxes) > 1:
        return False
    if len(boxes) == 1:
        return True
    keys = {key for box in boxes for key in box}
    for index, _ in enumerate(boxes[1:], start=1):
        if index not in keys:
            return False
    return True


canUnlockAll = can_unlock_all
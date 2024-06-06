#!/usr/bin/python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    visited = []
    queue = [0]
    while queue:
        for key in boxes[queue[0]]:
            if key not in queue and key not in visited:
                queue.append(key)
        visited.append(queue.pop(0))
    return len(visited) == len(boxes)

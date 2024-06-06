#!/usr/bin/python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    n = len(boxes)
    visited = []
    queue = [0]
    while queue:
        for key in boxes[queue[0]]:
            if key not in queue and key not in visited and key < n:
                queue.append(key)
        visited.append(queue.pop(0))
    return len(visited) == n

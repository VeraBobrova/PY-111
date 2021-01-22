"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

priority_queue = {}


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    priority_queue.setdefault(priority, [])
    priority_queue[priority].append(elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """

    new_list = sorted(priority_queue.keys())
    for i in new_list:
        if priority_queue[i]:
            return priority_queue[i].pop(0)


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if len(priority_queue[priority]) > ind:
        return priority_queue[priority][ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    priority_queue.clear()

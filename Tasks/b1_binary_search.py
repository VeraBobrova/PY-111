from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == elem:
            while mid > 0 and arr[mid - 1] == elem:
                mid -= 1
            return mid
        elif arr[mid] > elem:
            high = mid - 1
        else:
            low = mid + 1

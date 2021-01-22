from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, low=0, high=0) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    if low > high:
        return None
    if high == 0:
        high = len(arr) - 1

    mid = int((low + high) / 2)

    if arr[mid] == elem:
        while mid > 0 and arr[mid - 1] == elem:
            mid -= 1
        return mid
    elif arr[mid] > elem:
        return binary_search(elem, arr, low, mid - 1)
    else:
        return binary_search(elem, arr, mid + 1, high)

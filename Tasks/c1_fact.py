def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n == 1:
        return 1
    elif n < 1:
        raise ValueError
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 1:
        raise ValueError
    else:
        fact = 1
        for elem in range(1, n + 1):
            fact *= elem
        return fact

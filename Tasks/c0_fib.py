def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    number1 = 0
    number2 = 1
    counter = 1
    while counter < n:
        counter += 1
        number1, number2 = number2, number1 + number2
    return number2


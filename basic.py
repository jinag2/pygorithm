#
# Basic algorithm functions
#


def factorial(n):
    """
    Return the factorial of an integer.
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(6)
    720
    >>> factorial(6.0)
    Traceback (most recent call last):
    ValueError
    """
    if not isinstance(n, int):
        raise ValueError

    if n == 0:
        return 1
    elif n == 1:
        return 1

    return n * factorial(n - 1)


def fib(n):
    """
    Fibonacci Polynomials
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(9)
    34
    >>> fib(6.0)
    Traceback (most recent call last):
    ValueError
    """
    if not isinstance(n, int):
        raise ValueError

    if n == 0:
        return 0
    elif (n == 1) or (n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)


def _fib_dpa_helper(n, fib_result):
    if fib_result[n] >= 0:
        return fib_result[n]

    if n == 0:
        result = 0
    elif (n == 1) or (n == 2):
        result = 1
    else:
        result = _fib_dpa_helper(n - 1, fib_result) + _fib_dpa_helper(n - 2, fib_result)
    fib_result[n] = result
    return result


def fib_dpa(n):
    """
    Fibonacci Polynomials implemented with dynamic programming algorithm
    >>> fib_dpa(0)
    0
    >>> fib_dpa(1)
    1
    >>> fib_dpa(2)
    1
    >>> fib_dpa(9)
    34
    >>> fib_dpa(6.0)
    Traceback (most recent call last):
    ValueError
    """
    if not isinstance(n, int):
        raise ValueError

    fib_result = [-1] * (n + 1)
    return _fib_dpa_helper(n, fib_result)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

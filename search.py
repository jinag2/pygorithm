def binary_search(data, value):
    """
    >>> binary_search([], 23)
    False
    >>> binary_search([3, 10, 12, 18, 23, 35, 42, 51, 62, 79], 23)
    True
    >>> binary_search([3, 10, 12, 18, 23, 35, 42, 51, 62, 79], 47)
    False
    """
    if len(data) == 0:
        return False

    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if value == data[mid]:
            return True
        elif value < data[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()

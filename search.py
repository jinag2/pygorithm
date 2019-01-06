def binary_search(data, key):
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

    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if key == data[mid]:
            return True
        elif key < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


def interpolation_search(data, key):
    """
    >>> interpolation_search([], 23)
    False
    >>> interpolation_search([3, 10, 12, 18, 23, 35, 42, 51, 62, 79], 23)
    True
    >>> interpolation_search([3, 10, 12, 18, 23, 35, 42, 51, 62, 79], 47)
    False
    """
    if len(data) == 0:
        return False

    low = 0
    high = len(data) - 1
    while low <= high:
        mid = int(low + ((key - data[low]) / (data[high] - data[low])) * (high - low))
        if mid < low or mid > high:
            break
        if key == data[mid]:
            return True
        elif key < data[mid]:
            high = mid - 1
        elif key > data[mid]:
            low = mid + 1
        else:
            return False

    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()

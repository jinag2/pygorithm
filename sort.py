def bubble_sort(data):
    """
    Bob sort algorithm
    >>> bubble_sort([])
    []
    >>> bubble_sort([1])
    [1]
    >>> bubble_sort([4, 6, 2, 8, 9, 7])
    [2, 4, 6, 7, 8, 9]
    >>> bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> bubble_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def bubble_sort_pro(data):
    """
    Bob sort algorithm with a flag
    >>> bubble_sort_pro([])
    []
    >>> bubble_sort_pro([1])
    [1]
    >>> bubble_sort_pro([4, 6, 2, 8, 9, 7])
    [2, 4, 6, 7, 8, 9]
    >>> bubble_sort_pro([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> bubble_sort_pro([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    for i in range(len(data) - 1):
        exchange = False
        for j in range(len(data) - 1 - i):
            if data[j] > data[j+1]:
                exchange = True
                data[j], data[j+1] = data[j+1], data[j]
        if not exchange:
            break

    return data


def select_sort(data):
    """
    Selection sort algorithm
    >>> select_sort([])
    []
    >>> select_sort([1])
    [1]
    >>> select_sort([4, 6, 2, 8, 9, 7])
    [2, 4, 6, 7, 8, 9]
    >>> select_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> select_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    for i in range(len(data) - 1):
        max_idx = 0
        j = max_idx
        for j in range(1, len(data) - i):
            if data[j] > data[max_idx]:
                max_idx = j
        data[j], data[max_idx] = data[max_idx], data[j]
    return data


def select_sort2(data):
    """
    Selection sort algorithm
    >>> select_sort2([])
    []
    >>> select_sort2([1])
    [1]
    >>> select_sort2([4, 6, 2, 8, 9, 7])
    [2, 4, 6, 7, 8, 9]
    >>> select_sort2([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> select_sort2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    for i in range(len(data) - 1):
        max_idx = len(data) - 1 - i
        last_idx = max_idx
        exchange = False
        for j in range(0, last_idx):
            if data[j] > data[max_idx]:
                max_idx = j
                exchange = True
        if exchange:
            data[last_idx], data[max_idx] = data[max_idx], data[last_idx]
    return data


def insert_sort(data):
    """
    Insertion sort algorithm
    >>> insert_sort([])
    []
    >>> insert_sort([1])
    [1]
    >>> insert_sort([4, 6, 2, 7, 9, 8])
    [2, 4, 6, 7, 8, 9]
    >>> insert_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> insert_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    for i in range(1, len(data)):
        k = i
        for j in range(i):
            if data[j] > data[i]:
                k = j
                break
        if k != i:
            temp = data[k]
            data[k] = data[i]
            while k < i:
                temp, data[k + 1] = data[k + 1], temp
                k += 1
    return data


def insert_sort2(data):
    """
    A better implementation of insertion sort algorithm
    >>> insert_sort2([])
    []
    >>> insert_sort2([1])
    [1]
    >>> insert_sort2([4, 6, 2, 7, 9, 8])
    [2, 4, 6, 7, 8, 9]
    >>> insert_sort2([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> insert_sort2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    for i in range(1, len(data)):
        last = data[i]
        j = i
        while j >= 1 and data[j - 1] > last:
            data[j] = data[j - 1]
            j -= 1
        data[j] = last

    return data


def quick_sort(data):
    """
    Quick sort algorithm
    >>> quick_sort([])
    []
    >>> quick_sort([1])
    [1]
    >>> quick_sort([4, 6, 2, 7, 9, 8])
    [2, 4, 6, 7, 8, 9]
    >>> quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> quick_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    small_list = []
    key_list = []
    big_list = []
    key = data[0]
    for i in data:
        if i < key:
            small_list.append(i)
        elif i > key:
            big_list.append(i)
        else:
            key_list.append(i)

    return quick_sort(small_list) + key_list + quick_sort(big_list)


def _quick_sort2_helper(data, left, right):
    if left >= right:
        return data

    i = left + 1
    j = right
    while i < j:
        while i <= right and data[i] < data[left]:
            i += 1
        while j >= left and data[j] > data[left]:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]

    if data[j] < data[left]:
        data[left], data[j] = data[j], data[left]

    if i >= j:
        _quick_sort2_helper(data, left, j - 1)
        _quick_sort2_helper(data, j + 1, right)

    return data


def quick_sort2(data):
    """
    Quick sort algorithm
    >>> quick_sort2([])
    []
    >>> quick_sort2([1])
    [1]
    >>> quick_sort2([4, 6, 2, 7, 9, 8])
    [2, 4, 6, 7, 8, 9]
    >>> quick_sort2([35, 10, 42, 3, 79, 12, 62, 18, 51, 23])
    [3, 10, 12, 18, 23, 35, 42, 51, 62, 79]
    >>> quick_sort2([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> quick_sort2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    return _quick_sort2_helper(data, 0, len(data)-1)


def merge_sort(data):
    """
    Merge sort algorithm
    >>> merge_sort([])
    []
    >>> merge_sort([1])
    [1]
    >>> merge_sort([4, 6, 2, 7, 9, 8])
    [2, 4, 6, 7, 8, 9]
    >>> merge_sort([35, 10, 42, 3, 79, 12, 62, 18, 51, 23])
    [3, 10, 12, 18, 23, 35, 42, 51, 62, 79]
    >>> merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> merge_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_list = merge_sort(data[:mid])
    right_list = merge_sort(data[mid:])

    i = 0
    j = 0
    k = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            data[k] = left_list[i]
            i += 1
        else:
            data[k] = right_list[j]
            j += 1
        k += 1

    while i < len(left_list):
        data[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        data[k] = right_list[j]
        j += 1
        k += 1

    return data


def _heapify(data, n, i):
    parent = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and data[left] > data[parent]:
        parent = left
    if right < n and data[right] > data[parent]:
        parent = right
    if parent != i:
        data[parent], data[i] = data[i], data[parent]
        _heapify(data, n, parent)


def heap_sort(data):
    """
    Merge sort algorithm
    >>> heap_sort([])
    []
    >>> heap_sort([1])
    [1]
    >>> heap_sort([4, 6, 2, 7, 9, 8])
    [2, 4, 6, 7, 8, 9]
    >>> heap_sort([35, 10, 42, 3, 79, 12, 62, 18, 51, 23])
    [3, 10, 12, 18, 23, 35, 42, 51, 62, 79]
    >>> heap_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> heap_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    for i in range(len(data)//2 - 1, -1, -1):
        _heapify(data, len(data), i)

    for i in range(len(data) - 1, -1, -1):
        data[0], data[i] = data[i], data[0]
        _heapify(data, i, 0)

    return data


def radix_sort(data):
    """
    Merge sort algorithm
    >>> radix_sort([])
    []
    >>> radix_sort([1])
    [1]
    >>> radix_sort([4, 6, 2, 7, 9, 8])
    [2, 4, 6, 7, 8, 9]
    >>> radix_sort([59, 95, 7, 34, 60, 168, 171, 259, 372, 45, 88, 133])
    [7, 34, 45, 59, 60, 88, 95, 133, 168, 171, 259, 372]
    >>> radix_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> radix_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    max_num = max(data)

    exp = 1
    while max_num // exp:
        buckets = []
        for i in range(10):
            buckets.append([])

        for i in range(len(data)):
            buckets[(data[i] // exp) % 10].append(data[i])
        exp *= 10

        data = []
        for each in buckets:
            data += each

    return data


def shell_sort(data):
    """
    Shell sort algorithm
    >>> shell_sort([])
    []
    >>> shell_sort([1])
    [1]
    >>> shell_sort([4, 6, 2, 7, 9, 8])
    [2, 4, 6, 7, 8, 9]
    >>> shell_sort([10, 14, 73, 25, 23, 13, 27, 94, 33, 39, 25, 59, 94, 65, 82, 45])
    [10, 13, 14, 23, 25, 25, 27, 33, 39, 45, 59, 65, 73, 82, 94, 94]
    >>> shell_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> shell_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(data) <= 1:
        return data

    gap = len(data) // 2
    while gap > 0:
        for i in range(gap, len(data)):
            last = data[i]
            j = i
            while j >= gap and data[j - gap] > last:
                data[j] = data[j - gap]
                j -= gap
            data[j] = last
        gap = gap // 2

    return data


if __name__ == '__main__':
    import doctest
    doctest.testmod()

def main():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


def merge(arr, left_index, mid_index, right_index) -> list:
    """
    left arr: [left_index, mid_index)
    right arr: [mid_index, right_index)
    """

    #Из-за этого места была сильная просадка происводительност.
    # Потому что изначально копировал весь массив. На тестах терялась целая секунда
    new_arr = [None] * (right_index - left_index)  # copy of PART initial array

    k, i, j = left_index, left_index, mid_index
    while i < mid_index and j < right_index:
        if arr[i] <= arr[j]:
            new_arr[k - left_index] = arr[i]
            i += 1
        else:
            new_arr[k - left_index] = arr[j]
            j += 1
        k += 1

    while i < mid_index:
        new_arr[k - left_index] = arr[i]
        i += 1
        k += 1
    while j < right_index:
        new_arr[k - left_index] = arr[j]
        j += 1
        k += 1

    arr[left_index:right_index] = new_arr
    return arr


def merge_sort(arr, left_index, right_index):
    """
    merge sort list inplace
    """
    mid_index = left_index + (right_index - left_index) // 2
    # mid_index = (left_index + right_index) // 2
    if mid_index > left_index:
        merge_sort(arr, left_index, mid_index)
        merge_sort(arr, mid_index, right_index)
        _ = merge(arr, left_index, mid_index, right_index)


if __name__ == '__main__':
    main()

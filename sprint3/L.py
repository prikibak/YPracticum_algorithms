import sys


def main():
    days_count = int(read_line())
    accumulations = list(map(int, read_line().split()))
    price = int(read_line())
    # prev_res_index, res_index = None, len(accumulations)-1
    # while res_index != prev_res_index and res_index != -1:
    #     prev_res_index = res_index
    #     res_index = binarySearch(accumulations, price, 0, res_index+1)
    # res_index = binarySearch(accumulations, price, 0, len(accumulations))
    res_index = binarySearch3(accumulations, price, 0, len(accumulations), -1)
    res_index2 = binarySearch3(accumulations, 2*price, 0, len(accumulations), -1)
    # if res_index != -1:
    #     res_index += 1
    # if res_index2 != -1:
    #     res_index2 += 1
    print(res_index, res_index2)


def read_line():
    return sys.stdin.readline()


def binarySearch(arr, x, left, right):
    print(arr, arr[left:right], x, left, right)
    if right <= left: # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x: # центральный элемент — искомый
        return mid
    elif x < arr[mid]: # искомый элемент меньше центрального
                       # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else: # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)


# def binarySearch2(arr, x, left, right):
#     # print(arr, arr[left:right], x, left, right)
#     if right <= left: # промежуток пуст
#         return -1
#     mid = (left + right) // 2
#     # diff = right - left
#     if arr[mid] >= x:
#         return mid
#     # elif diff == 1 and arr[left] >= x:
#     #     return left
#     # elif diff == 2:
#     #     if arr[left] >= x:
#     #         return left
#     #     elif arr[right - 1] >= x:
#     #         return right - 1
#     elif x < arr[mid]: # искомый элемент меньше центрального
#                        # значит следует искать в левой половине
#         return binarySearch2(arr, x, left, mid)
#     # else: # иначе следует искать в правой половине
#     #     return binarySearch2(arr, x, mid + 1, right)


def binarySearch2(arr, x, left, right):
    # print(arr, arr[left:right], x, left, right)
    if right <= left: # промежуток пуст
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x:
        return mid
    else:
        return binarySearch2(arr, x, mid + 1, right)


def binarySearch3(arr, x, left, right, indx):
    # print(arr, arr[left:right], x, left, right)
    if right <= left: # промежуток пуст
        return indx
    mid = (left + right) // 2
    if arr[mid] >= x:
        indx = mid
    if x <= arr[mid]:
        return binarySearch3(arr, x, left, mid, indx)
    else:
        return binarySearch3(arr, x, mid + 1, right, indx)


if __name__ == '__main__':
    main()
